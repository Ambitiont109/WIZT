# Generated by Django 2.2.1 on 2019-05-27 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_auto_20190526_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='product_id',
            field=models.CharField(default='testid', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='subscribed_customer_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='subscribed_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='subscribed_plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='backend.Plan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='subscribed_token_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='subscription_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='SubscribeTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subscribe_email', models.EmailField(max_length=254)),
                ('subscribed_token_id', models.CharField(max_length=100)),
                ('plan_name', models.CharField(max_length=100)),
                ('plan_price', models.FloatField()),
                ('plan_product_id', models.CharField(max_length=100)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
