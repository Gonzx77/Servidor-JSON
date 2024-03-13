import requests
import json

obtener = requests.get("http://172.16.100.138:5500")
print(obtener.json())


empleadoNuevo = {
        "codigo": 3,
        "nombre": "Miguel Angel",
        "apellido": "Castro Escamilla"
}

print(empleadoNuevo)


obtener = requests.post("http://172.16.100.138:5500", data=json.dumps(empleadoNuevo))
print(obtener.json())