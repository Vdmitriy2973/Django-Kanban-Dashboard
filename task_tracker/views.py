from django.utils.timezone import localtime

from task_tracker.forms import UserProfileForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.set_password(request.POST["password"])
            user.save()

            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте введенные данные.')
    else:
        form = UserProfileForm()

    return render(request, 'task_tracker/auth/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'task_tracker/auth/login.html', {'form': form})

@login_required
def logout_user(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Вы вышли из системы!")
        return redirect('login')
    return render(request, 'task_tracker/auth/logout.html')

@login_required
def user(request):
    return render(request, 'task_tracker/personal_account.html')


@login_required
def task_board(request):
    context = {"current_time": localtime().strftime("%Y-%m-%d")}
    return render(request,'task_tracker/kanban_board.html',context)
