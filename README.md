
#Descripcion del fichero y Funciones del programa:

EL fichero json contiene un array concesionarios de toyota en estados unidos con información de localización, contacto, servicios e inventario. Este presenta la siguiente estructura:

```
ROOT (Array)
│
└── concesionario (Object)
    │
    ├── code (string)
    ├── name (string)
    ├── city (string)
    ├── state (string)
    ├── address1 (string)
    ├── zipCode (string)
    ├── latitude (number)
    ├── longitude (number)
    │
    ├── general (object)
    │   ├── url (string|null)
    │   ├── phone (string)
    │   ├── parsedPhone (string|null)
    │   └── hours (array)
    │       └── array
    │           └── string
    │
    ├── service (object)
    │   ├── url (string|null)
    │   ├── phone (string|null)
    │   ├── parsedPhone (string|null)
    │   └── hours (array|null)
    │
    ├── tda (object)
    │   ├── code (string)
    │   └── name (string)
    │
    ├── region (object)
    │   ├── regionCode (number)
    │   └── success (boolean)
    │
    ├── dealerAttributes (array)
    │   └── string
    │
    └── inventario (object)
        │
        └── modelo (object)
            ├── stock (number)
            ├── precio_base (number)
            ├── colores (array[string])
            ├── motorizaciones (array[string])
            └── extras (array[string])
```

Podemos ver mas clara la estructuracon el siguiente ejemplo:

```
{
  {
    "code": "37130",
    "general": {
      "url": null,
      "phone": "7172643359",
      "parsedPhone": null,
      "hours": [
        [
          "Closed"
        ],
        [
          "0900,2100"
        ],
        [
          "0900,2100"
        ],
        [
          "0900,2100"
        ],
        [
          "0900,2100"
        ],
        [
          "0900,2100"
        ],
        [
          "0900,1800"
        ]
      ]
    },
    "pma": false,
    "city": "Chambersburg",
    "service": {
      "url": "http://www.fitzgeraldtoyota.com/serviceappt.html",
      "phone": "8008117519",
      "parsedPhone": null,
      "hours": null
    },
    "encodedDashedStateName": "PA",
    "encodedDashedName": "Fitzgerald-Toyota",
    "state": "PA",
    "parts": null,
    "latitude": 39.925868,
    "tda": {
      "code": "CAT10",
      "name": "Central Atlantic Toyota"
    },
    "fax": "7172648805",
    "finance": null,
    "address1": "1436 Lincoln Way East",
    "address2": null,
    "zipCode": "17201",
    "encodedDashedCity": "Chambersburg",
    "phone": "7172643359",
    "distance": 49.43,
    "name": "Fitzgerald Toyota",
    "url": "http://www.fitzgeraldtoyota.com",
    "region": {
      "regionCode": 80,
      "success": false
    },
    "longitude": -77.621128,
    "dealerAttributes": [
      "CUV",
      "EL",
      "TTC"
    ],
    "inventario": {
      "Camry": {
        "precio_base": 32000,
        "colores": [
          "Negro",
          "Gris",
          "Plata"
        ],
        "motorizaciones": [
          "2.5 Hybrid"
        ],
        "extras": [
          "Cuero",
          "Sistema premium audio"
        ],
        "stock": 16
      },
      "Highlander": {
        "precio_base": 42000,
        "colores": [
          "Blanco",
          "Negro",
          "Gris"
        ],
        "motorizaciones": [
          "2.5 Hybrid AWD"
        ],
        "extras": [
          "7 plazas",
          "Techo panor\u00e1mico",
          "Asistencia offroad"
        ],
        "stock": 18
      },
      "Yaris": {
        "precio_base": 18000,
        "colores": [
          "Blanco",
          "Rojo",
          "Azul"
        ],
        "motorizaciones": [
          "1.5 Hybrid"
        ],
        "extras": [
          "Apple CarPlay",
          "Android Auto"
        ],
        "stock": 20
      },
      "Prius": {
        "precio_base": 30000,
        "colores": [
          "Blanco",
          "Azul",
          "Negro"
        ],
        "motorizaciones": [
          "2.0 Hybrid"
        ],
        "extras": [
          "Modo el\u00e9ctrico",
          "Carga inal\u00e1mbrica"
        ],
        "stock": 20
      }
     }
  },
  {Otro concesionario}
}
```

##Las Funcionalidades del menu de el programa cumpliran las siguientes tareas:

1. Mostrar todos los concesionarios indicando nombre, ciudad y estado.

2. Mostrar cuántos modelos distintos hay en el inventario de cada concesionario.

3. Pedir un precio base minimo y uno maximo y mostrar los coches que se pueden optener en este rango

4. Pedir un modelo y mostrar en qué concesionarios está disponible y sus motorizaciones.

5. Mostrar un listado de todos los modelos registrados con el numero de unidades en stock, motorizaciones, colores y extras en total sumando los datos de todos los concesionarios. Esta lista estará ordenada de mayor a menor por el numero de unidades.


#Registro del Proyecto

##Decisiones tomadas:

-La carga del fichero es delegada a una funcion y no se contempla directamente en el codigo del fichero principal.

-Debido a la compejidad de la funcionalidad 3, se a dividido la ejecucion de esta en 3 funciones, una que recorre los datos y puede imprimir por pantalla, una que se asegura de optener los datos de el usuario y una ultima a la que se le delega la compracion de los precion dentro del rango.

##Dificutades encontradas:

-Dificultad al orientar el codigo para la funcionalidad 3, debido a que al principio se trato de poner solo los modelos en ese rango, lo cual no solo acarreaba mas complejidad al tener que agrupar los modelos iguales a trabes de cada concesionario sino que podia ser impreciso, ya que en cada concesionario el precio de un unico modelo puede variar, asi que al final se a optado por proporcinar todas las unidades que encajan en el rango junto a su precio y el concesionario al que pertenecen.

##Descripcion de las funciones:

-cargarDatos: Trata de recoger los datos del json y devuelve una lista con los datos, si hay un error contemplado como que el fichero no esta o no se puede leer correctamente dara un error al usuario y hara que el programa cierre usando la libreria sys.

-listarConcesionarios: Recorre todos los elementos de la lista y por cada uno optiene nombre, ciudad y estado y los va mostrando por pantalla, al final tambien muestra el total de concesionarios que hay.

-contarModelosConcesionario: Recorre todos los elementos de datos y por cada uno optiene el nombre y extrae el largo del inventario de este y los imprime al usuario.

-optenerPrecios: Trata de optener el rango de precio pidiendolo al uduario, si el usuario introduce datos de tipo erroneo o un rango inposible se le da un error y se detiene el programa. Si no hay errores devuelve el rango

-comprobarRangoPrecio: Recibe un precio_base, uno maximo y uno minimo, comprueba si el base esta comprendido entre estos y si es asi devuelve True.

-mostrarCochesEnRangoPrecio: Revisa todos los coches de todos los concesionarios y si estos tienen un precio base dentro de un rango pedido a el usuario imprime por pantalla el modelo del cohce, su precio basey en que concesionario se encuentra.

