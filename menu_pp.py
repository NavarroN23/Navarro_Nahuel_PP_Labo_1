'''
Navarro Nahuel DIV: A211-TT
'''

from funciones_pp import *
from funciones_archivo_pp import *
bandera_archivo = False
bandera_archivo_ordenado = False
while True:
    mostrar_menu_opciones()
    opcion = int(input("Ingrese una opción (0-6): "))
    while opcion < 0 or opcion > 6:
        print("Opción no válida. Intente nuevamente.")
        opcion = int(input("Ingrese una opción (0-6): "))

    match opcion:
        case 1:
            respuesta = input("usar nombre por defecto del archivo? (si/no): ").lower()
            if respuesta == "no":
                path = input("Ingrese el nombre del archivo: ").lower()
                path += ".json"
                lista_servicios = leer_json(path)
                normalizar_datos(lista_servicios)
                bandera_archivo = True
            else:
                path = "parciales\data.json"
                lista_servicios = leer_json(path)
                normalizar_datos(lista_servicios)
                bandera_archivo = True
        case 2:
            if bandera_archivo:
                print("id_servicio || descripcion || tipo || precioUnitario || cantidad || totalServicio ||")
                print(mostrar_columnas(lista_servicios))
            else:
                print("No se cargo ningun archivo (opcion 1).")
        case 3:
            if bandera_archivo:
                asignar_totales(lista_servicios)
            else:
                print("No se cargo ningun archivo (opcion 1).")
        case 4:
            if bandera_archivo:
                lista_filtrada = filtrar_tipo(lista_servicios)
                nombre_archivo = input("Ingrese el nombre del archivo: ").lower()
                nombre_archivo += ".json"
                guardar_json(lista_filtrada,nombre_archivo)
            else:
                print("No se cargo ningun archivo (opcion 1).")
        case 5:
            if bandera_archivo:
                lista_ordenada = ordenar_por_clave(lista_servicios,"descripcion")
                print("id_servicio || descripcion || tipo || precioUnitario || cantidad || totalServicio ||")
                print(mostrar_columnas(lista_ordenada))
                bandera_archivo_ordenado = True
            else:
                print("No se cargo ningun archivo (opcion 1).")
        case 6:
            if bandera_archivo:
                if bandera_archivo_ordenado:
                    nombre_archivo = input("Ingrese el nombre del archivo: ").lower()
                    nombre_archivo += ".json"
                    guardar_json(lista_ordenada,nombre_archivo)
                else:
                    print("No se ordeno ningun archivo (opcion 5).")
            else:
                print("No se cargo ningun archivo (opcion 1).")
        case 0:
            break