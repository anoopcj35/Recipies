# Generated by Django 4.1.4 on 2023-02-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0002_register_password_register_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=72),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=67),
        ),
    ]