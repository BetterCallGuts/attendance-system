# Generated by Django 4.2.7 on 2023-12-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_student_aca_id_alter_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='aca_em',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Student email'),
        ),
    ]