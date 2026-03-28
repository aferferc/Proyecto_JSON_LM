import json
import sys

def cargarDatos(ruta):
    try:
        with open(ruta, encoding='utf-8') as fichero:
            datos = json.load(fichero)
        return datos
    except FileNotFoundError:
        print('Error al cargar datos: no se encontró el fichero ', ruta)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print('Error al leer el JSON: ', e)
        sys.exit(1)
    
def listarConcesionarios(datos):
    for i in range(len(datos)):
        c = datos[i]
        print('Nombre: ', c['name'], '| Ciudad: ', c['city'], '| Estado: ', c['state'])
    print('Total:', len(datos), 'concesionarios')