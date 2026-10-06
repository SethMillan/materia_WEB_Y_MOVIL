from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .reglas import elegir_medio

def hola(request):
    return HttpResponse("Hola. Plataforma de entregas (aún sin pedidos).")

def estado(request):
    return JsonResponse({
        "servicio": "entregas",
        "version": 1,
        "medios_disponibles": ["camioneta", "moto", "bicicleta", "dron"],
    })

def cotizar(request):
    km = request.GET.get("km")
    kg = request.GET.get("kg")

    # Verificar que existan
    if km is None:
        return JsonResponse({"error": "Falta el parametro km"}, status=400)
    if kg is None:
        return JsonResponse({"error": "Falta el parametro kg"}, status=400)

    # Intentar convertir
    try:
        km = float(km)
    except ValueError:
        return JsonResponse(
            {"error": "El parametro km debe ser un numero"},
            status=400
        )
    try:
        kg = float(kg)
    except ValueError:
        return JsonResponse(
            {"error": "El parametro kg debe ser un numero"},
            status=400
        )

    # Verificar negativos
    if km < 0:
        return JsonResponse(
            {"error": "Los kilometros no pueden ser negativos"},
            status=400
        )
    if kg < 0:
        return JsonResponse(
            {"error": "Los kilogramos no pueden ser negativos"},
            status=400
        )

    medio, motivo = elegir_medio(km, kg)

    return JsonResponse({
        "km": km,
        "kg": kg,
        "medio": medio,
        "motivo": motivo
    })