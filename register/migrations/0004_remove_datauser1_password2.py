# Generated by Django 4.1.2 on 2022-11-01 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_datauser1_datauser2_delete_datauser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datauser1',
            name='password2',
        ),
    ]
