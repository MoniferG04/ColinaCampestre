# Generated by Django 4.1.5 on 2023-01-17 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id_lotes', models.AutoField(primary_key=True, serialize=False)),
                ('ancho', models.IntegerField()),
                ('largo', models.IntegerField()),
                ('matricula', models.TextField()),
                ('precio', models.IntegerField()),
                ('zona', models.TextField()),
                ('estado', models.CharField(choices=[('Vendido', 'Vendido'), ('Disponible', 'Disponible'), ('Reservado', 'Reservado')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_identificacion', models.TextField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('telefono', models.TextField()),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.TextField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasenna', models.CharField(max_length=25)),
                ('rol', models.CharField(choices=[('Propietario', 'Propietario'), ('Cliente', 'Cliente'), ('Administrador', 'Administrador')], max_length=13)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Bloqueado', 'Bloqueado')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genera', to='app.lote')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicita', to='app.persona')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registra', to='app.usuario'),
        ),
        migrations.AddField(
            model_name='lote',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiene', to='app.servicio'),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_facturar', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('precio', models.FloatField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paga', to='app.persona')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genera', to='app.servicio')),
            ],
        ),
    ]
