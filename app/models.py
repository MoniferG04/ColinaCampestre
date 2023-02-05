from django.db import models

# Create your models here.
#modelo usuario
class Usuario(models.Model):
    ROL=(('Propietario','Propietario'),('Cliente','Cliente'),("Administrador","Administrador"))
    ESTADO=(('Activo','Activo'),('Bloqueado','Bloqueado'))
    id_usuario=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    rol=models.CharField(max_length=13,choices=ROL)
    estado=models.CharField(max_length=11,choices=ESTADO)
    def __str__(self):
        return self.email
        
#modelo persona
class Persona(models.Model):
    GENERO_OPCIONES=(('Masculino','Masculino'),('Femenino','Femenino'))
    id_identificacion=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.CharField(max_length=10)
    fecha_nacimiento=models.DateField()
    genero=models.CharField(max_length=9,choices=GENERO_OPCIONES)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='registra')
    def __str__(self):
        return self.nombre

#modelo servicios
class Servicio(models.Model):
    id_servicio=models.AutoField(primary_key=True)
    tipo=models.CharField(max_length=100)
    precio=models.IntegerField()
    def __str__(self):
        return self.tipo

#modelo lote
class Lote(models.Model):
    ESTADO=(('Vendido','Vendido'),('Disponible','Disponible'),('Reservado','Reservado'))
    id_lotes=models.AutoField(primary_key=True)
    ancho=models.IntegerField()
    largo=models.IntegerField()
    matricula=models.CharField(max_length=20)
    precio=models.IntegerField()
    zona=models.CharField(max_length=20)
    estado=models.CharField(max_length=10,choices=ESTADO)
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

#modelos fecha    
class Fechas(models.Model):
    ESTADO=(('Bloqueado','Bloqueado'),('Reservado','Reservado'))
    id_fecha=models.AutoField(primary_key=True)
    date=models.DateField()
    estado=models.CharField(max_length=11,choices=ESTADO)
    def __str__(self):
         return str(self.id_fecha)

#modelos reserva
class Reserva(models.Model):
    HORA=(('8:00','8:00'),('9:00','9:00'),('10:00','10:00'),('11:00','11:00'),('12:00','12:00'),('13:00','13:00'),('14:00','14:00'),('15:00','15:00'),('16:00','16:00'),('17:00','17:00'),('18:00','18:00'))
    id_reserva=models.AutoField(primary_key=True)
    dia=models.DateField()
    hora=models.CharField(max_length=11,choices=HORA)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='solicita')
    lote=models.ForeignKey(Lote,on_delete=models.CASCADE,related_name='genera')
    def __str__(self):
        return str(self.id_reserva)
