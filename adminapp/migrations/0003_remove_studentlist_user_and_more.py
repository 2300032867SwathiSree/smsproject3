# Generated by Django 5.0.7 on 2024-09-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_studentlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentlist',
            name='user',
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='Register_Number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
