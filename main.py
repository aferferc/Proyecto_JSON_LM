from funciones import *

menu = '''Opciones disponibles:
1.Listar todos los concesionarios
2.Contar modelos por concesionario
3.Filtrar modelos por rango de precio
4.Buscar concesionarios por modelo
5.Resumen global de modelos (stock total)
6.Ver media de unidades disponibles de un modelo en los concesionarios
7.Filtrar modelos por rango de precio en una ciudad concreta
8.Salir'''

datos = cargarDatos('toyota-modificado.json')

verMenu = True

while verMenu:
    print(menu)
    try:
        opcion = int(input('Seleccione una opción (entrada numérica): '))
    except ValueError:
        print('Error: La opción debe ser un numero')
        continue
    if opcion == 1:
        listarConcesionarios(datos)
    elif opcion == 2:
        contarModelosConcesionario(datos)
    elif opcion == 3:
        mostrarCochesEnRangoPrecio(datos)
    elif opcion == 4:
        mostrarModeloCoincidente(datos)
    elif opcion == 5:
        resumenGlobalModelos(datos)
    elif opcion == 6:
        VerMediaStock(datos)
    elif opcion == 7:
        mostrarCochesEnRangoPrecioCiudad(datos)
    elif opcion == 8:
        verMenu = False
    else:
        print('Error: Debes introducir una opción comprendida en el menú')
        
