from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return HttpResponse("<h1>Hola mundo</h1>")

def mapa_view(request):
    return render(request, 'mapa.html')

def inicio(request):
    return render(request, 'inicio.html')

def procesar_busqueda(request):
    query = request.GET.get('query', '').lower()
    
    # Simulamos que la IA reconoce estos lugares de GDL
    if "minerva" in query:
        datos = {
            "lat": 20.6744, 
            "lng": -103.3873, 
            "mensaje": "¡Claro! Te llevo a la Glorieta de la Minerva."
        }
    elif "hospicio" in query:
        datos = {
            "lat": 20.6769, 
            "lng": -103.3371, 
            "mensaje": "Visitando el Hospicio Cabañas..."
        }
    else:
        # Si la IA no entiende, manda un error
        datos = {"error": "No lo encontré"}
        
    return JsonResponse(datos)