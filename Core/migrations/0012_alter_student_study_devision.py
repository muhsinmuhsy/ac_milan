# Generated by Django 4.1.5 on 2023-04-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0011_remove_student_id_proof2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='study_Devision',
            field=models.CharField(max_length=2, null=True),
        ),
    ]