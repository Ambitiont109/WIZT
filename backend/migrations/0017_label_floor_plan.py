# Generated by Django 2.2.1 on 2019-06-21 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20190619_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='floor_plan',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.FloorPlan'),
        ),
    ]