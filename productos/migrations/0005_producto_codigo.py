# Generated by Django 5.1 on 2024-11-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_producto_marca_producto_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(default='prod-xxx', max_length=9),
        ),
    ]