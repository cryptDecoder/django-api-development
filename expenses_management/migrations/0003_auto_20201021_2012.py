# Generated by Django 3.0.7 on 2020-10-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_management', '0002_auto_20201021_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
