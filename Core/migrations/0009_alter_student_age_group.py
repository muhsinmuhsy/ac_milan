# Generated by Django 4.1.5 on 2023-04-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_alter_student_age_group_alter_student_study_devision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age_group',
            field=models.CharField(max_length=100),
        ),
    ]