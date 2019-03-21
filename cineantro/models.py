from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.

class Institucion(models.Model):
	nombre = models.CharField(max_length=50, blank=1, null=1)
	direccion = models.CharField(max_length=50, blank=1, null=1)

	def __str__(self):
		return self.nombre

class Paciente(models.Model):
	#Choices
	SEXO_CHOICE = (
		(1,'Masculino'),
		(2,'Femenino'),
	)

	EC_CHOICE = (
		(1,'Soltero'),
		(2,'Casado'),
		(3,'Divorciado'),
		(4,'Viudo'),
	)

	#Fields
	nombre = models.CharField(max_length=50, blank=1, null=1)
	apellidos = models.CharField(max_length=50, blank=1, null=1)
	institucion = models.ForeignKey(Institucion, null=1)
	f_nac = models.DateField(blank=1, null=1)
	sexo = models.IntegerField(choices=SEXO_CHOICE, default='1', blank=1)
	domicilio = models.CharField(max_length=50, blank=1, null=1)
	tel = models.IntegerField(default='0', blank=1)
	ci = models.IntegerField(default='0', blank=1)
	seguro = models.CharField(max_length=50, blank=1, null=1)
	procedencia = models.CharField(max_length=50, blank=1, null=1)
	ocupacion = models.CharField(max_length=50, blank=1, null=1)
	ec = models.IntegerField(choices=EC_CHOICE, default='1', blank=1)
	enfermedad = models.CharField(max_length=50, blank=1, null=1)
	sintomas = models.CharField(max_length=50, blank=1, null=1)
	signos = models.CharField(max_length=50, blank=1, null=1)
	sindromes = models.CharField(max_length=50, blank=1, null=1)
	a_personales = models.CharField(max_length=50, blank=1, null=1)
	a_patologicos = models.CharField(max_length=50, blank=1, null=1)
	a_nopatologicos = models.CharField(max_length=50 ,blank=1, null=1)
	a_hereditarios = models.CharField(max_length=50, blank=1, null=1)
	a_presuntivo = models.CharField(max_length=50, blank=1, null=1)
	d_definitivo = models.CharField(max_length=50, blank=1, null=1)
	interconsulta = models.CharField(max_length=50, blank=1, null=1)
	imagen = models.ImageField(blank=1, null=1)
	#institucion = models.CharField(max_length=50, blank=1, null=1)
	#institucion = models.ManyToManyField(Institucion)
	#institucion = models.ForeignKey(Institucion)
	
	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		view_name = "detail"
		return reverse(view_name, kwargs={"pk": self.id})

class Examen(models.Model):
	fecha = models.DateField(blank=1, null=1)
	estatura = models.IntegerField(default='0', blank=1)
	peso = models.IntegerField(default='0', blank=1)
	edad = models.IntegerField(default='0', blank=1)
	pa = models.CharField(max_length=10, blank=1, null=1)
	fc = models.IntegerField(default='0', blank=1)
	fr = models.IntegerField(default='0', blank=1)
	t_oral = models.IntegerField(default='0', blank=1)
	t_rectal = models.IntegerField(default='0', blank=1)
	tratamiento = models.TextField(blank=1, null=1)
	#paciente = models.OnetoManyfield(Paciente)
	pacientes = models.ForeignKey(Paciente)

	def __str__(self):
		return str(self.fecha)

class IMC(models.Model):
	peso = models.IntegerField(default='0', blank=1)
	estatura = models.IntegerField(default='0', blank=1)
	examen =  models.ForeignKey(Examen)

	def __str__(self):
		return self.examen

class Antropometrico(models.Model):
	actividad = models.IntegerField(default='0', blank=1)
	porcentaje_grasa = models.IntegerField(default='0', blank=1)
	observacion = models.TextField(blank=1, null=1)
	examen =  models.ForeignKey(Examen)

	def __str__(self):
		return self.examen

class Porcentaje(models.Model):
	porcentaje_grasa_deseado = models.IntegerField(default='0', blank=1)
	antropometrico = models.ForeignKey(Antropometrico)

	def __str__(self):
		return self.antropometrico