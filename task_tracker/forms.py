from django import forms
from .models import User, Task
from django.contrib.auth.forms import AuthenticationForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email','age']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'})
    )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','task_description','category','created_at','expire_at','author']