# Generated by Django 4.0.5 on 2022-06-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indvaltech', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='esicDoc',
            field=models.FileField(upload_to='media/'),
        ),
    ]
