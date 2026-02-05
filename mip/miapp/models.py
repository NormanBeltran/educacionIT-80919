from django.db import models
import datetime

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    inscriptos = models.IntegerField()
    profesor = models.CharField(max_length=50)
    adjunto = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.inscriptos}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ESPECIALIDADES = (
        (1, "Python"),
        (2, "HTML"),
        (3, "JavaScript"),
        (4, "Django"),
        (5, "C"),
    )
    especialidad = models.IntegerField(choices=ESPECIALIDADES)
    fecha_nacimiento = models.DateField(default=datetime.date(2000, 1, 1))

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"    

    class Meta:
        verbose_name_plural = "Profesores"
        verbose_name = "Profesor"


