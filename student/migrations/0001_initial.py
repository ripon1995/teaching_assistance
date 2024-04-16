# Generated by Django 4.2.8 on 2024-04-15 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0005_alter_course_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('institution', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=30)),
                ('father_contact_number', models.CharField(max_length=30)),
                ('start_date', models.DateField(auto_now=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]