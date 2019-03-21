from django.contrib import admin

from cineantro.models import Paciente, Institucion, Examen, IMC, Antropometrico, Porcentaje

# Register your models here.

admin.site.register(Institucion)
admin.site.register(Paciente)
admin.site.register(Examen)
admin.site.register(IMC)
admin.site.register(Antropometrico)
admin.site.register(Porcentaje)