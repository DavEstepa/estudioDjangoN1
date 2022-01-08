from django.shortcuts import render
from django.http import HttpResponse
#----NOTAS----
#Cada vista ha de retornar una respuesta al cliente. En este caso se ayuda de HttpResponse
#quien se encargará de darle el formato adecuado al msn que se desea retornar en el body del
#cifrado http (Hypertext Transfer Protocol-Protocolo de Transferencia de Hipertexto).

def index(request):
    return HttpResponse("Hola Mundo. Se encuentra en el index (VISTA) de encuestas.")