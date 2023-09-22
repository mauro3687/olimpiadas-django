from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    id_usuario=models.BigAutoField(primary_key=True)
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    password=models.CharField(max_length=20)




class Enfermero (models.Model):
    dni_enfermero = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    sexo = models.CharField(max_length=10, choices=(('M', 'Masculino'), ('F', 'Femenino')))
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20, blank=True)  
    estado = models.IntegerField(choices=((1, 'Activo'), (0, 'Inactivo')))

class Paciente(models.Model):
    dni_paciente=models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10, choices=(('M', 'Masculino'), ('F', 'Femenino')))
    tipo_sangre = models.CharField(max_length=5 )
    patologia = models.CharField(max_length=255, blank=True)  
    alergias = models.CharField(max_length=255, blank=True)  
    telefono = models.CharField(max_length=20, blank=True)  
    direccion = models.CharField(max_length=255)
    dni_enfermero = models.ForeignKey(Enfermero, on_delete=models.CASCADE)

class Antecedentes(models.Model):
    dni_paciente = models.BigIntegerField()
    diagnostico = models.TextField()
    motivo = models.CharField(max_length=255)
    tratamiento = models.CharField(max_length=255)
    medicacion = models.CharField(max_length=255)
    fecha_antec = models.DateField()




class Llamada(models.Model):

    id_llamada = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=255)
    fecha_hora_llamada = models.DateTimeField()
    fecha_hora_atendida = models.DateTimeField()
    dni_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Tipo_llamada (models.Model):
    id_tipo_llamada = models.AutoField(primary_key=True)
    tipo_llamada = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    id_tipo_llamada = models.ForeignKey(Tipo_llamada, on_delete=models.CASCADE)
    dni_enfermero = models.ForeignKey(Enfermero, on_delete=models.CASCADE)
    dni_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.IntegerField(choices=((1, 'Activo'), (0, 'Inactivo')))
class Area_llamada(models.Model):
    id_area_llamada= models.AutoField(primary_key=True)
    id_area= models.ForeignKey(Area,on_delete=models.CASCADE)
    
    id_llamada=models.ForeignKey(Llamada,on_delete=models.CASCADE)