# Generated by Django 4.1.5 on 2023-01-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rename_teacher_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]
