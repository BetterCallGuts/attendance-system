# Generated by Django 4.2.7 on 2023-12-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_student_levels'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='attend',
            field=models.TextField(blank=True, null=True),
        ),
    ]
