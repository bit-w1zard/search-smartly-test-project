# Generated by Django 4.2.10 on 2024-02-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poi_id', models.CharField(max_length=100)),
                ('poi_name', models.CharField(max_length=255)),
                ('poi_category', models.CharField(max_length=100)),
                ('poi_latitude', models.FloatField()),
                ('poi_longitude', models.FloatField()),
                ('poi_ratings', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
