# Generated by Django 4.2.7 on 2023-11-13 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={},
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='username',
        ),
    ]