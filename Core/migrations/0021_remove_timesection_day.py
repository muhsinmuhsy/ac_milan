# Generated by Django 4.1.5 on 2023-04-20 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0020_remove_attendance_students_attendance_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesection',
            name='day',
        ),
    ]