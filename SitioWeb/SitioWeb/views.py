import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from SitioWeb.models import Lugar
from django.shortcuts import redirect


def index(request):
    return HttpResponse("<h1>Hola mundo</h1>")


def mapa_view(request):
    return render(request, 'mapa.html')


def mapa_db_view(request):
    producto = request.GET.get('producto', '').strip()

    # obtener lista de productos existentes (excluir vacíos)
    productos = list(
        Lugar.objects.exclude(producto='').values_list('producto', flat=True).distinct()
    )

    if producto:
        qs = Lugar.objects.filter(producto__icontains=producto)
    else:
        qs = Lugar.objects.all()

    lugares = list(qs.values('nombre', 'descripcion', 'latitud', 'longitud', 'producto'))
    lugares_json = json.dumps(lugares)
    return render(request, 'mapa.html', {
        'lugares_json': lugares_json,
        'productos': productos,
        'selected_producto': producto,
    })


def agregar_lugar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        producto = request.POST.get('producto', '')
        lat = request.POST.get('latitud')
        lng = request.POST.get('longitud')

        try:
            lat_f = float(lat)
            lng_f = float(lng)
            Lugar.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                producto=producto,
                latitud=lat_f,
                longitud=lng_f
            )
            return redirect(f'/mapa/?producto={producto}')
        except Exception as e:
            return HttpResponse(f'Error: {e}', status=400)

    return render(request, 'agregar.html')


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