# Generated by Django 2.2.1 on 2019-06-08 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20190606_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends_count',
        ),
    ]