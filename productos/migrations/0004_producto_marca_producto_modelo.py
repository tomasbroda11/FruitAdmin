# Generated by Django 5.1 on 2024-11-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='modelo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
