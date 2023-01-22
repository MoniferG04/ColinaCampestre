from django.db import models

# Create your models here.
#modelo usuario
class Usuario(models.Model):
    ROL=(('Propietario','Propietario'),('Cliente','Cliente'),("Administrador","Administrador"))
    ESTADO=(('Activo','Activo'),('Bloqueado','Bloqueado'))
    id_usuario=models.AutoField(primary_key=True)
    username=models.TextField()
    email=models.EmailField()
    password=models.CharField(max_length=25)
    rol=models.CharField(max_length=13,choices=ROL)
    estado=models.CharField(max_length=11,choices=ESTADO)
    def __str__(self):
        return self.correo
        
#modelo persona
class Persona(models.Model):
    GENERO_OPCIONES=(('Masculino','Masculino'),('Femenino','Femenino'))
    id_identificacion=models.TextField(primary_key=True)
    nombre=models.TextField()
    apellido=models.TextField()
    telefono=models.TextField()
    fecha_nacimiento=models.DateField()
    genero=models.CharField(max_length=9,choices=GENERO_OPCIONES)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='registra')
    def __str__(self):
        return self.nombre

#modelo servicios
class Servicio(models.Model):
    id_servicio=models.AutoField(primary_key=True)
    tipo=models.TextField()
    precio=models.IntegerField()
    def __str__(self):
        return self.tipo

#modelo lote
class Lote(models.Model):
    ESTADO=(('Vendido','Vendido'),('Disponible','Disponible'),('Reservado','Reservado'))
    id_lotes=models.AutoField(primary_key=True)
    ancho=models.IntegerField()
    largo=models.IntegerField()
    matricula=models.TextField()
    precio=models.IntegerField()
    zona=models.TextField()
    estado=models.CharField(max_length=10,choices=ESTADO)
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE,related_name='tiene')
    def __str__(self):
        return self.matricula

#model factura
class Factura(models.Model):
    id_facturar=models.AutoField(primary_key=True)
    fecha=models.DateField()
    precio=models.FloatField()
    persona=models.ForeignKey(Persona,on_delete=models.CASCADE,related_name='paga')
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE,related_name='genera')
    def __str__(self):
        return self.id_facturar
    
#modelos reserva
class Reserva(models.Model):
    id_reserva=models.AutoField(primary_key=True)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    persona=models.ForeignKey(Persona,on_delete=models.CASCADE,related_name='solicita')
    lote=models.ForeignKey(Lote,on_delete=models.CASCADE,related_name='genera')
    def __str__(self):
        return self.id_reserva