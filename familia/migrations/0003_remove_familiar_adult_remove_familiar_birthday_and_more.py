# Generated by Django 4.0.4 on 2022-05-18 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0002_rename_curso_familiar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='adult',
        ),
        migrations.RemoveField(
            model_name='familiar',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='familiar',
            name='email',
        ),
    ]