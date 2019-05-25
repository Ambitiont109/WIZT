# Generated by Django 2.2.1 on 2019-05-25 12:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_label_ar_mark_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='device_token',
            field=models.CharField(default='device-token', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='device_type',
            field=models.CharField(default='device_type', max_length=50),
            preserve_default=False,
        ),
    ]