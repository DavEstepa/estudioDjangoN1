import datetime

from django.db import models
from django.utils import timezone
# A model is the single, definitive source of information about your data. 
#It contains the essential fields and behaviors of the data you’re storing

#A many-to-one relationship. Requires two positional arguments: the class to which 
#the model is related and the on_delete option.
#When an object referenced by a ForeignKey is deleted, Django will emulate the behavior 
#of the SQL constraint specified by the on_delete argument
#ON DELETE CASCADE constraint is used in MySQL to delete the rows from the child table automatically, 
#when the rows from the parent table are deleted

from django.db import models


class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    pub_fecha = models.DateTimeField('Fecha publicada')

    def __str__(self):
        return self.pregunta_texto

    def fue_publicado_recientemente(self):
        return self.pub_fecha >= timezone.now() - datetime.timedelta(days=1)

class Eleccion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    eleccion_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.eleccion_texto