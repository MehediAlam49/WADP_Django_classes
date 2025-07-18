# Generated by Django 5.2.3 on 2025-06-21 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infomodel',
            name='phohe',
        ),
        migrations.AddField(
            model_name='infomodel',
            name='phone',
            field=models.CharField(max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
