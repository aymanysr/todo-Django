# Generated by Django 4.2.8 on 2023-12-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
