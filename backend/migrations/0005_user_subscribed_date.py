# Generated by Django 2.2.1 on 2019-06-05 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20190605_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscribed_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]