# Generated by Django 5.0.1 on 2024-02-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_category'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='category.category'),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
