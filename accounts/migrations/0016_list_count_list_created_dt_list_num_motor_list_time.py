# Generated by Django 4.1.5 on 2023-02-05 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_list_category_list_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='count',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='num_motor',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AddField(
            model_name='list',
            name='time',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
