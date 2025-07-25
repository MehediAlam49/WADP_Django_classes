# Generated by Django 5.2.4 on 2025-07-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobNestApp', '0002_customusermodel_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('salary', models.PositiveBigIntegerField(null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('deadline', models.DateField(null=True)),
            ],
        ),
    ]
