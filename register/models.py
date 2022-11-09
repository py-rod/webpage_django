from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DataUser1(models.Model):
    user = models.CharField(max_length=50)
    email = models.EmailField()
    password1 = models.CharField(max_length=200)
    def __str__(self):
        return f"email: {self.email}"
    
    

class DataUser2(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    def __str__(self):
        return f"UserName: {self.user}"
    

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    create = models.DateTimeField(auto_now_add=True)
    datecomplete = models.DateTimeField(null=True)
    important = models.BooleanField(default=True)
    user = models.ForeignKey(User(), on_delete=models.CASCADE)
    def __str__(self):
        return f"Title: {self.title} | User: {self.user}"