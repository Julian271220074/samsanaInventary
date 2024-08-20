# Generated by Django 5.1 on 2024-08-18 00:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionar_productos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Producto', models.CharField(max_length=255)),
                ('precio_Producto', models.FloatField()),
                ('cantidad_Venta', models.FloatField()),
                ('total_Venta_Realizada', models.FloatField(editable=False)),
                ('estado', models.BooleanField(default=True)),
                ('saldo_Inicial', models.FloatField(blank=True, null=True)),
                ('saldo_Actual', models.FloatField(blank=True, null=True)),
                ('fecha_Apertura', models.DateTimeField()),
                ('fecha_Cierre', models.DateTimeField(blank=True, null=True)),
                ('id_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas_has_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionar_productos.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionar_ventas.venta')),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='productos',
            field=models.ManyToManyField(through='gestionar_ventas.Ventas_has_producto', to='gestionar_productos.producto'),
        ),
    ]