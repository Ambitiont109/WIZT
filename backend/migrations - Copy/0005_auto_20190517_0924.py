# Generated by Django 2.2 on 2019-05-17 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20190517_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friend_friends', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_users', to=settings.AUTH_USER_MODEL),
        ),
    ]