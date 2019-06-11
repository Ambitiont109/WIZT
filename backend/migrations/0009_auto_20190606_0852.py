# Generated by Django 2.2.1 on 2019-06-05 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20190706_0421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='subscribed_date',
            new_name='calling_date',
        ),
        migrations.AddField(
            model_name='user',
            name='label_cnt',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='user',
            name='photo_cnt',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='label_in_use',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo_in_use',
            field=models.IntegerField(default=0),
        ),
    ]