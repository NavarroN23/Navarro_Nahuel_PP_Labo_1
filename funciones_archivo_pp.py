'''
Navarro Nahuel DIV: A211-TT
'''
import json

def leer_json(path: str):
    """
    Lee un archivo JSON y retorna su contenido.

    Parámetros:
    path (str): Ruta del archivo JSON.

    Retorna:
    retorno (list|bool): Lista con los datos del archivo JSON si se lee correctamente, de lo contrario False.
    """
    try:
        with open(path, 'r') as archivo:
            data = json.load(archivo)
            retorno = data
    except:
        print("ERROR, NO SE PUDO ABRIR EL ARCHIVO.")
        retorno = False

    return retorno

def guardar_json(lista: list, path: str):
    """
    Guarda una lista en un archivo JSON.

    Parámetros:
    lista (list): Lista de diccionarios que se guardarán en el archivo.
    path (str): Ruta del archivo JSON.

    Retorna:
    None
    """
    try:
        with open(path, 'w+') as archivo:
            json.dump(lista, archivo, ensure_ascii=False, indent=4)
        print(f"Lista guardada exitosamente en '{path}'.")
    except:
        print(f"Ocurrió un error al guardar el archivo JSON")

def normalizar_datos(lista):
    """
    Normaliza los datos en la lista de servicios para asegurarse de que tienen los tipos de datos correctos.

    Parámetros:
    lista (list): Lista de diccionarios que contiene los servicios.

    Retorna:
    None
    """
    bandera_dato_normalizado = False
    if lista:
        if len(lista) > 0:
            for servicio in lista:
                if type(servicio['id_servicio']) != int: 
                    servicio['id_servicio'] = int(servicio['id_servicio'])
                    bandera_dato_normalizado = True
                if type(servicio['tipo']) != int: 
                    servicio['tipo'] = int(servicio['tipo'])
                    bandera_dato_normalizado = True
                if type(servicio['precioUnitario']) != float:
                    servicio['precioUnitario'] = float(servicio['precioUnitario'])
                    bandera_dato_normalizado = True
                if type(servicio['cantidad'] != int):
                    servicio['cantidad'] = int(servicio['cantidad'])
                    bandera_dato_normalizado = True
                if type(servicio['totalServicio'] != int):
                    servicio['totalServicio'] = int(servicio['totalServicio'])
                    bandera_dato_normalizado = True
        
            if bandera_dato_normalizado == True:
                print("Datos normalizados")
        else:
            print("Error: Lista de servicios vacía")