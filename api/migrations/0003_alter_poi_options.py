# Generated by Django 4.2.10 on 2024-02-16 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_poi_poi_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poi',
            options={'verbose_name': 'POI', 'verbose_name_plural': 'POIs'},
        ),
    ]