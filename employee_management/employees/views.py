from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import User

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']  # Нужно будет хэшировать
            try:
                user = User.objects.get(username=username, password=password)
                response = redirect('/employees/')
                response.set_cookie('user_id', user.id)  # Устанавливаем cookie
                return response
            except User.DoesNotExist:
                return render(request, 'employees/login.html', {'form': form, 'error': 'Неверные данные'})
    else:
        form = LoginForm()
    return render(request, 'employees/login.html', {'form': form})