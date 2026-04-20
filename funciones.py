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
    for c in datos:
        print('Nombre: ', c['name'], '| Ciudad: ', c['city'], '| Estado: ', c['state'])
    print('Total:', len(datos), 'concesionarios')
            
def contarModelosConcesionario(datos):
    for c in datos:
        print('Nombre: ', c['name'], ' | Modelos disponibles: ', len(c['inventario']))
        
def optenerPrecios():
    try:
        pmax = float(input('Introduce el precio maximo: '))
        pmin = float(input('Introduce el precio minimo: '))
        if pmax < pmin:
            print('Error el precio maximo debe ser sueperior o igual al minimo')
            sys.exit(1)
        return pmax, pmin
    except ValueError:
        print('Error el precio debe ser un numero')
        sys.exit(1)
        
def comprobarRangoPrecio(precio, pmax, pmin):
    if precio >= pmin and precio <= pmax:
        return True

def mostrarCochesEnRangoPrecio(datos):
    pmax, pmin = optenerPrecios()
    for c in datos:
        for coche, info in c['inventario'].items():
            if comprobarRangoPrecio(info['precio_base'], pmax, pmin):
                print('Modelo: ', coche, ' | Precio Base: ', info['precio_base'], ' | Concesionario: ', c['name'])

def optenerModelo(datos):
    modelo = str(input('Introduzca el modelo deseado: '))
    if comprobarModeloEnInventario(datos, modelo):
        return modelo
    else:
        print("Error: No se ha podido encontrar ningun registro de este modelo")
        sys.exit(1)

def comprobarModeloEnInventario(datos, modelo):
    for c in datos:
        for coche in c['inventario']:
            if coche.lower() == modelo.lower():
                return True

def mostrarModeloCoincidente(datos):
    modelo = optenerModelo(datos)
    for c in datos:
        for coche, info in c['inventario'].items():
            if coche.lower() == modelo.lower():
                motorizaciones = ''
                for m in info['motorizaciones']:
                    motorizaciones = motorizaciones + ' ' + m
                print('Modelo: ', coche, ' | Motorizaciones:', motorizaciones, ' | Concesionario: ', c['name'])

def resumenGlobalModelos(datos):
    Global = {}
    for c in datos:
        for coche, info in c['inventario'].items():
            if coche not in Global:
                Global[coche] = {'stock': 0, 'motorizaciones': [], 'colores': [], 'extras': []}
            Global[coche]['stock'] += info['stock']
            for m in info['motorizaciones']:
                if m not in Global[coche]['motorizaciones']:
                    Global[coche]['motorizaciones'].append(m)
            for col in info['colores']:
                if col not in Global[coche]['colores']:
                    Global[coche]['colores'].append(col)
            for e in info['extras']:
                if e not in Global[coche]['extras']:
                    Global[coche]['extras'].append(e)
    for coche in sorted(Global, key=lambda coche: Global[coche]['stock'], reverse=True):
        print('Modelo: ', coche, ' | Stock: ', Global[coche]['stock'], ' | Motorizaciones: ', len(Global[coche]['motorizaciones']), ' | Colores: ', len(Global[coche]['colores']), ' | Extras: ', len(Global[coche]['extras']))
        