# Generated by Django 4.1.5 on 2023-02-05 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fechas',
            fields=[
                ('id_fecha', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('estado', models.CharField(choices=[('Bloqueado', 'Bloqueado'), ('Reservado', 'Reservado')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id_lotes', models.AutoField(primary_key=True, serialize=False)),
                ('ancho', models.IntegerField()),
                ('largo', models.IntegerField()),
                ('matricula', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('zona', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('Vendido', 'Vendido'), ('Disponible', 'Disponible'), ('Reservado', 'Reservado')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('rol', models.CharField(choices=[('Propietario', 'Propietario'), ('Cliente', 'Cliente'), ('Administrador', 'Administrador')], max_length=13)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Bloqueado', 'Bloqueado')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.DateField()),
                ('hora', models.CharField(choices=[('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00')], max_length=11)),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genera', to='app.lote')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicita', to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_identificacion', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=9)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registra', to='app.usuario')),
            ],
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
