# Generated by Django 4.2.7 on 2023-11-13 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_student_options_alter_teacher_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teachers',
        ),
    ]
