# Generated by Django 4.2.7 on 2023-12-03 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_level_course_faculty_course_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='levels',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.level'),
        ),
    ]
