# Generated by Django 4.2.8 on 2023-12-31 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todos_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedtodolist',
            name='TodoList',
        ),
        migrations.RemoveField(
            model_name='todos',
            name='TodoList',
        ),
        migrations.AddField(
            model_name='sharedtodolist',
            name='todo_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.todolist'),
        ),
        migrations.AddField(
            model_name='todos',
            name='todo_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.todolist'),
        ),
    ]
