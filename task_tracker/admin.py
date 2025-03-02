from django.contrib import admin
from .models import User, Task




@admin.register(User)
class UserList(admin.ModelAdmin):
    list_display = ('id','username','first_name','middle_name','last_name','email','age','created_at')


@admin.register(Task)
class TaskList(admin.ModelAdmin):
    list_display = ('id','task_name','task_description','category','created_at','expire_at','author')