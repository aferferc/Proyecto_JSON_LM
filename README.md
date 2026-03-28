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

##Las Funciones del menu de el programa cumpliran las siguientes tareas:

1. Mostrar todos los concesionarios indicando nombre, ciudad y estado.

2. Mostrar cuántos modelos distintos hay en el inventario de cada concesionario.

3. Pedir un precio base minimo y uno maximo y mostrar los coches que se pueden optener en este rango

4. Pedir un modelo y mostrar en qué concesionarios está disponible y sus motorizaciones.

5. Mostrar un listado de todos los modelos registrados con el numero de unidades en stock, motorizaciones, colores y extras en total sumando los datos de todos los concesionarios. Esta lista estará ordenada de mayor a menor por el numero de unidades.


#Registro del Proyecto

##Decisiones tomadas:

-La carga del fichero es delegada a una funcion y no se contempla directamente en el codigo del fichero principal.

##Dificutades encontradas:



##Descripcion de las funciones:

-cargarDatos: Trata de recoger los datos del json y devuelve una lista con los datos, si hay un error contemplado como que el fichero no esta o no se puede leer correctamente dara un error al usuario y hara que el programa cierre usando la libreria sys

-listarConcesionarios: Recorre todo el largo de la lista de concesionarios y por cada uno optiene nombre, ciudad y estado y los va mostrando por pantalla, al final tambien muestra el total de concesionarios que hay


