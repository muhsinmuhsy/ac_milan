# Generated by Django 4.1.5 on 2023-04-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0019_remove_attendance_status_remove_attendance_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='students',
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ManyToManyField(to='Core.student'),
        ),
        migrations.DeleteModel(
            name='StudentAttendance',
        ),
    ]