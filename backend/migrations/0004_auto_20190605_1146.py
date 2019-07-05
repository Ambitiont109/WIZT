# Generated by Django 2.2.1 on 2019-06-05 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20190605_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='device_token',
        ),
        migrations.AddField(
            model_name='user',
            name='target_arn',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]