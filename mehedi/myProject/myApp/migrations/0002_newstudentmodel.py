# Generated by Django 5.2.1 on 2025-05-27 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newstudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
