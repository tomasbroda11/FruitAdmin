# Generated by Django 5.1 on 2024-10-05 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('porcentaje_ganancia', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipo_medida', models.CharField(choices=[('unidad', 'Unidad'), ('peso', 'Peso (kg)')], default='unidad', max_length=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria')),
            ],
        ),
    ]
