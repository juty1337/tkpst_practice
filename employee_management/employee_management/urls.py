from django.contrib import admin
from django.urls import path, include
from employees.views import register, CustomLoginView, logout_view, employee_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', employee_list, name='employee_list'),  # Главная страница перенаправляет на список сотрудников
    #path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/', include('employees.urls')),  # API маршруты
]