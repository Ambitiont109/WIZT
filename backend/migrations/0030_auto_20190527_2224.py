# Generated by Django 2.2.1 on 2019-05-27 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_subscribetransaction_subscription_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sharelabel',
            unique_together={('label', 'share_by', 'share_to')},
        ),
    ]
