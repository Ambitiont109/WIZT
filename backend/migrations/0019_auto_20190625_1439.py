# Generated by Django 2.2.1 on 2019-06-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_auto_20190625_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainmodel',
            name='embedding',
            field=models.CharField(max_length=1000),
        ),
    ]
