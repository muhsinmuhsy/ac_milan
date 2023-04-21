# Generated by Django 4.1.5 on 2023-04-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0015_attendance_delete_attends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='present',
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Late'), ('E', 'Excused')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(),
        ),
    ]
