from django.http import HttpResponse,JsonResponse


def hola(request):
    return HttpResponse("Hola. Plataforma de entregas (aún sin pedidos).")

def estado(request):
    return JsonResponse({
        "servicio": "entregas",
        "version": 1,
        "medios_disponibles": ["camioneta", "moto", "bicicleta", "dron"],
    })