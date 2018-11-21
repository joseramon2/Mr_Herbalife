# Generated by Django 2.1 on 2018-11-13 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('descripcion', models.CharField(blank=True, max_length=50, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='AccesoriosActividades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('accesorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.Accesorios', verbose_name='AccesoriosACT a Actividades')),
            ],
        ),
        migrations.CreateModel(
            name='ActividadAlerta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('descripcion', models.CharField(blank=True, max_length=50, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='ActividadesRealizadas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('observaciones', models.TextField(blank=True, verbose_name='observaciones')),
                ('realizado', models.DateTimeField(auto_now=True, verbose_name='realizado')),
                ('actividades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.Actividades', verbose_name='Realizadas a Reportes')),
            ],
        ),
        migrations.CreateModel(
            name='Codigos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('creado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuartos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('descripcion', models.CharField(blank=True, max_length=50, verbose_name='descripcion')),
                ('codigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Room.Codigos', verbose_name='Codigo a Codigos')),
            ],
        ),
        migrations.CreateModel(
            name='FocosDeActividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('colores', models.CharField(max_length=7, verbose_name='colores')),
                ('descripcion', models.CharField(blank=True, max_length=50, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Pisos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('descripcion', models.CharField(blank=True, max_length=50, verbose_name='descripcion')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creado', models.DateTimeField(auto_now=True, verbose_name='creado')),
                ('observaciones', models.TextField(blank=True, verbose_name='observaciones')),
                ('inicio', models.DateTimeField(verbose_name='inicio')),
                ('fin', models.DateTimeField()),
                ('cuarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.Cuartos')),
            ],
        ),
        migrations.AddField(
            model_name='cuartos',
            name='piso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.Pisos', verbose_name='Cuarto a Pisos'),
        ),
        migrations.AddField(
            model_name='actividadesrealizadas',
            name='reporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.Reportes', verbose_name='Realizadas a Reportes'),
        ),
        migrations.AddField(
            model_name='actividadalerta',
            name='actividadRealizada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.ActividadesRealizadas', verbose_name='Focos a Reporte'),
        ),
        migrations.AddField(
            model_name='actividadalerta',
            name='foco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.FocosDeActividad', verbose_name='Reporte de focos a los focos'),
        ),
        migrations.AddField(
            model_name='accesoriosactividades',
            name='actividades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.Actividades', verbose_name='AccesoriosACT a Actividades'),
        ),
        migrations.AddField(
            model_name='accesorios',
            name='codigo',
            field=models.ForeignKey(null=True, on_delete=True, to='Room.Codigos', verbose_name='Accesorios a Codigo'),
        ),
        migrations.AddField(
            model_name='accesorios',
            name='cuarto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.Cuartos', verbose_name='Accesorios a Cuarto'),
        ),
    ]
