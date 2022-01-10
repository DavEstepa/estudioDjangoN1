from django.shortcuts import render
from django.http import HttpResponse

#----NOTAS----
#Cada vista ha de retornar una respuesta al cliente. En este caso se ayuda de HttpResponse
#quien se encargará de darle el formato adecuado al msn que se desea retornar en el body del
#cifrado http (Hypertext Transfer Protocol-Protocolo de Transferencia de Hipertexto).

#GENERACION DE LA APLICACION: python manage.py startapp polls
#GENERACION DE TABLA EN BASE DE DATOS: python manage.py migrate
#The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables

#By running makemigrations, you’re telling Django that you’ve made some changes to your models 
#(in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
#python manage.py makemigrations polls
def index(request):
    return HttpResponse("Hola Mundo. Se encuentra en el index (VISTA) de encuestas.")