'''
Navarro Nahuel DIV: A211-TT
'''

def mostrar_columnas(lista_dict, id_servicio = True, descripcion = True,tipo = True, precioUnitario = True, cantidad = True,
                     totalServicio = True):
    """
    genera un string de los servicios en la lista de diccionarios con las columnas seleccionadas.

    Parámetros:
    lista_dict (list): Lista de diccionarios que contien los servicios.
    id_servicio (bool): Si se debe mostrar la columna 'id_servicio'. Por defecto es True.
    descripcion (bool): Si se debe mostrar la columna 'descripcion'. Por defecto es True.
    tipo (bool): Si se debe mostrar la columna 'tipo'. Por defecto es True.
    precioUnitario (bool): Si se debe mostrar la columna 'precioUnitario'. Por defecto es True.
    cantidad (bool): Si se debe mostrar la columna 'cantidad'. Por defecto es True.
    totalServicio (bool): Si se debe mostrar la columna 'totalServicio'. Por defecto es True.

    Retorna:
    msj (str): string que contiene todos los datos del diccionario ordenado en columnas.
    """
    msj = ""
    for dict in lista_dict:
        if(id_servicio): msj += str(dict["id_servicio"]) + " || " 
        if(descripcion): msj += dict["descripcion"] + " || " 
        if(tipo): msj += str(dict["tipo"]) + " || " 
        if(precioUnitario): msj += str(dict["precioUnitario"]) + " || " 
        if(cantidad): msj += str(dict["cantidad"]) + " || " 
        if(totalServicio): msj += str(dict["totalServicio"]) + " || " 
        msj += "\n--------------------------------------------------------------------------------------------\n"
    return msj

def asignar_totales(lista: list):
    """
    Asigna el total calculado para cada servicio en la lista. El total es el producto del precio unitario y la cantidad.

    Parámetros:
    lista (list): Lista de diccionarios que contiene los servicios.

    Retorna:
    None
    """
    for servicio in lista:
        calcular_totales = lambda precioU, cantidad: precioU * cantidad
        servicio["totalServicio"] = calcular_totales(servicio["precioUnitario"], servicio["cantidad"])

def filtrar_tipo(lista:list):
    """
    Filtra los servicios de la lista según el tipo de servicio seleccionado por el usuario.

    Parámetros:
    lista (list): Lista de diccionarios que contiene los servicios.

    Retorna:
    lista_tipo_filtrado (list): Lista de diccionarios con los servicios filtrados por el tipo seleccionado.
    """
    lista_tipo_filtrado = []
    tipo_selec = int(input("Ingrese el numero del tipo de servicio que desea (1-MINORISTA, 2-MAYORISTA, 3-EXPORTAR): "))
    while tipo_selec < 1 or tipo_selec > 3:
        tipo_selec = int(input("ERRRO, vuelva a ingresar el numero del tipo de servicio (1-MINORISTA, 2-MAYORISTA, 3-EXPORTAR): "))
    
    for servicio in lista:
        if servicio["tipo"] == tipo_selec:
            lista_tipo_filtrado.append(servicio) 

    return lista_tipo_filtrado

def ordenar_por_clave(lista_diccionarios:list, clave:str):
    """
    Ordena una lista de diccionarios por una clave específica.

    Parámetros:
    lista_diccionarios (list): Lista de diccionarios que contiene los servicios.
    clave (str): Clave por la cual se ordenará la lista.

    Retorna:
    lista_ordenada (list): Lista de diccionarios ordenada por la clave especificada.
    """
    lista_ordenada = sorted(lista_diccionarios, key = lambda diccionario: diccionario[clave])
    return lista_ordenada


def mostrar_menu_opciones():
    print('''
          Menú de Opciones:
            1- Cargar archivo.
            2- Imprimir lista.
            3- Asignar totales.
            4- Filtrar por tipo.         
            5- Mostrar servicios.
            6- Guardar servicios.
            0- Salir
          ''')