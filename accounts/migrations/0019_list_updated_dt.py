# Generated by Django 4.1.5 on 2023-02-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_list_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='updated_dt',
            field=models.DateTimeField(null=True),
        ),
    ]