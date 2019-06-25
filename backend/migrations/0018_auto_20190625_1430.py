# Generated by Django 2.2.1 on 2019-06-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_label_floor_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainmodel',
            name='embedding',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='image',
            field=models.URLField(max_length=150),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='thumbnail',
            field=models.URLField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
    ]