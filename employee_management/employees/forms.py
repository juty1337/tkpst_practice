from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")