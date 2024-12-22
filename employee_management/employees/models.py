from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    pass



class Project(models.Model):
    id = models.AutoField(primary_key=True)  # Уникальный идентификатор проекта
    head_categories = models.ManyToManyField(
        'Category', related_name='head_projects', verbose_name="Головные категории", null=True,
    )  # Ссылка на несколько головных категорий проекта
    name = models.CharField(max_length=255, verbose_name="Имя проекта")  # Название проекта
    owners = models.ManyToManyField(CustomUser, related_name='owned_projects', verbose_name="Владельцы", null=True)  # Владельцы проекта
    tg_token = models.CharField(max_length=255, verbose_name="Token TG")  # Токен Telegram бота

    def __str__(self):
        return self.name

class Category(models.Model):
    button_name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='categories', verbose_name="Проект")  # Связь с проектом
    message = models.TextField(blank=True, default='')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_categories', verbose_name="Владелец")
    def save(self, *args, **kwargs):
        # Если категория не имеет родителя, значит, она головная
        if self.parent is None:
            # Проверяем, есть ли project_id, если нет, создаём новый проект
            if self.project_id is None:
                self.project_id = self.generate_project_id()

            # Сначала сохраняем категорию, чтобы потом можно было добавить её в head_categories
            super().save(*args, **kwargs)

            # Устанавливаем текущую категорию как головную для проекта (добавляем в head_categories)
            self.project_id.head_categories.add(self)
        else:
            # Если есть родитель, наследуем project_id от родителя
            self.project_id = self.parent.project_id
            super().save(*args, **kwargs)

        # Если есть дочерние элементы, устанавливаем им тот же project_id
        if self.parent is None:
            for child in self.children.all():
                child.project_id = self.project_id
                child.save()

    def generate_project_id(self):
        # Создаём новый проект и возвращаем его
        return Project.objects.create(name=f"Project for {self.button_name}")

    def __str__(self):
        return self.button_name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    post = models.CharField(max_length=100)
    date_of_employment = models.CharField(max_length=10)

    phone_number = models.CharField(max_length=12)
    address = models.TextField()
    position = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name 