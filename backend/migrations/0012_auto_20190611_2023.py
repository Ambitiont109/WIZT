# Generated by Django 2.2.1 on 2019-06-11 11:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20190609_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=150)),
                ('thumbnail', models.URLField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Train')),
            ],
            options={
                'db_table': 'train_images',
            },
        ),
        migrations.AddIndex(
            model_name='trainimage',
            index=models.Index(fields=['train'], name='train_image_train_i_08efe3_idx'),
        ),
    ]