import json

def cargarDatos(ruta):
    try:
        with open(ruta, encoding='utf-8') as fichero:
            datos = json.load(fichero)
        return datos
    except FileNotFoundError:
        print('Error al cargar datos: no se encontró el fichero ', ruta)
        return []
    except json.JSONDecodeError as e:
        print('Error al leer el JSON: ', e)
        return []