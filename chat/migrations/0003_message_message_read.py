# Generated by Django 3.0 on 2019-12-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20191206_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_read',
            field=models.BooleanField(default=False),
        ),
    ]
