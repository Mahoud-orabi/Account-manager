# Generated by Django 4.1.5 on 2023-02-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_list_updated_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='created_by',
            field=models.CharField(max_length=50, null=True),
        ),
    ]