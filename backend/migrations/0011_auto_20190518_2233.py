# Generated by Django 2.2.1 on 2019-05-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20190518_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]