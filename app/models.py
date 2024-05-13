from django.db import models

# Create your models here.
class Profesor (models.Model):
    rut = models.CharField(max_length=9,primary_key=True)
    nombre = models.CharField(max_length=50, null=False,blank=False)
    apellido = models.CharField(max_length=50, null=False,blank=False)
    # activo = bool(default=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modifiacion_registro = models.DateTimeField(auto_now_add=True)
    creado_por = models.CharField( max_length=50)

class Curso (models.Model):
    codigo = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50, null=False,blank=False)
    version = models.IntegerField()
    profesor_id = models.ManyToManyField('Profesor', related_name='curso', null=True, blank=True, on_delete=models.PROTECT)

class Estudiante(models.Model):
    rut = models.CharField(max_length=9,primary_key=True)
    nombre = models.CharField(max_length=50, null=False,blank=False)
    apellido = models.CharField(max_length=50, null=False,blank=False)
    #a mi parecer hace falta algo parecido a este campo:
    # curso_id = models.ManyToOneRel('Curso', related_name='estudiante', null=True, blank=True, on_delete=models.PROTECT)
    fecha_nac = models.CharField(max_length=50, null=False,blank=False)
    # activo = bool(default=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modifiacion_registro = models.DateTimeField(auto_now_add=True)
    creado_por = models.CharField( max_length=50)

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50, null=False,blank=False)
    numero = models.IntegerField(max_length=10, null=False,blank=False)
    depto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50, null=False,blank=False)
    ciudad = models.CharField(max_length=50, null=False,blank=False)
    region = models.CharField(max_length=50, null=False,blank=False)
    estudiante_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    


