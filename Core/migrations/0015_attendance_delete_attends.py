# Generated by Django 4.1.5 on 2023-04-19 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0014_remove_center_timesection_timesection_center'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('present', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.student')),
                ('time_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.timesection')),
            ],
        ),
        migrations.DeleteModel(
            name='Attends',
        ),
    ]