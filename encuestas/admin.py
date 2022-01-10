from django.contrib import admin

#---NOTAS

#python manage.py createsuperuser

from .models import Pregunta

admin.site.register(Pregunta)