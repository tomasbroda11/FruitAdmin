# Generated by Django 5.1 on 2024-10-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_pedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('en espera', 'En espera'), ('procesado', 'Procesado'), ('entregado', 'Entregado')], default='en espera', max_length=20),
        ),
    ]