# Generated by Django 5.1 on 2024-10-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='provincia',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
