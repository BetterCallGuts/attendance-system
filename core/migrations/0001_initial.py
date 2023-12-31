# Generated by Django 4.2.7 on 2023-12-10 15:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Course name')),
                ('coden', models.CharField(default='palce holder', max_length=255, verbose_name='Code name')),
                ('Term', models.CharField(blank=True, choices=[('1', 'First term'), ('2', 'Second term')], max_length=255, null=True)),
                ('starting_date', models.DateField(blank=True, default=datetime.datetime.now, editable=False, null=True)),
                ('ending_date', models.DateField(blank=True, default=datetime.datetime.now, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Student name')),
                ('aca_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='ID')),
                ('aca_em', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Student email')),
                ('password', models.CharField(blank=True, help_text='Will be id if blank', max_length=255, null=True, verbose_name='Student password')),
                ('Date_ofj', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Date of join')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.faculty')),
                ('levels', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.level')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourseRel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attend', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Intructor name')),
                ('ins_course', models.ManyToManyField(blank=True, to='core.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Days',
            field=models.ManyToManyField(blank=True, to='core.days'),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='inst',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.level'),
        ),
    ]
