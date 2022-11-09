from django.contrib import admin
from .models import DataUser1, DataUser2, Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("create", )

# Register your models here.
admin.site.register(Task, TaskAdmin)



