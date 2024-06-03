# Generated by Django 4.2.8 on 2024-05-31 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_capacity'),
        ('attendance', '0004_alter_attendance_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]