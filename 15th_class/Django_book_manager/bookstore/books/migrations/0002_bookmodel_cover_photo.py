# Generated by Django 5.2.3 on 2025-06-16 05:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='cover_photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/photos'),
            preserve_default=False,
        ),
    ]
