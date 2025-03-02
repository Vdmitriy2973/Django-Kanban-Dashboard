from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Модель пользователя"""

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username


class Task(models.Model):
    task_name = models.CharField(max_length=50,null=False)
    task_description = models.CharField(max_length=150,null=False)
    category = models.CharField(max_length=20,null=False,default='upcoming')
    created_at = models.DateTimeField()
    expire_at = models.DateTimeField()
    author = models.CharField(max_length=40, null=False)