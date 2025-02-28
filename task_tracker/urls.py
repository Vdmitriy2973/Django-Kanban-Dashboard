from django.urls import path

from . import views

urlpatterns = [
    path('',views.task_board, name='dashboard'),
    path('account', views.user, name='home'),
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout')
]
