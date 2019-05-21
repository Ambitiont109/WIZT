# Generated by Django 2.2.1 on 2019-05-18 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20190518_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sharelabel',
            name='share_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_labels_by_me', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sharelabel',
            name='share_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_labels_to_me', to=settings.AUTH_USER_MODEL),
        ),
    ]
