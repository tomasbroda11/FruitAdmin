# Generated by Django 5.1 on 2024-08-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.TextField(blank=True, null=True),
        ),
    ]
