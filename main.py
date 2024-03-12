import requests
import json

obtener = requests.get("http://172.16.100.132:5500")
print(obtener.json())


empleadoNuevo = {
    {
        "codigo": 3,
        "nombre": "Miguel Angel",
        "apellido": "Castro Escamilla"
    },
    {
        "codigo": 4,
        "nombre": "Maria Sol",
        "apellido": "Pinzon"
    }
}

obtener = requests.post("http://172.16.100.132:5500")
print(obtener.json())
