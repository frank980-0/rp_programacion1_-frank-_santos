'''1. Generar una función que calcule la media geométrica de filas o columnas de una matriz
cuadrada.'''

def medida_geometrica(matriz:list, estado = 0):
    '''esta funcion recibe por parametro una matriz que se asume es cuadrada y
    el parametros estado sirve para poder saber que se quiere calcular si las columnas o las filas
    estado = 0 se calcula las columnas 
    estado = 1 se calcula las filas
    y todo esto retorna las medias geometricas de cada uno en el main'''
    n = len(matriz)
    medias_geo = []

    if estado == 0:
        for columnas in range(n):
            producto = 1
            for fila in range(n):
                producto *= matriz[fila][columnas]
            
            media = producto ** (1/n)
            medias_geo.append(media)
    elif estado == 1:
        for fila in range(n):
            producto = 1
            for columnas in range (n):
                producto *= matriz[fila][columnas]
            media = producto ** (1/n)
            medias_geo.append(media)
    return medias_geo