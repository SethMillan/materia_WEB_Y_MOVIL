import json
import urllib.request

url = "http://127.0.0.1:8000/entregas/cotizar/?km=5&kg=2"
with urllib.request.urlopen(url) as respuesta:
    datos = json.load(respuesta)

print("Medio sugerido:", datos["medio"])
print("Motivo:", datos["motivo"])