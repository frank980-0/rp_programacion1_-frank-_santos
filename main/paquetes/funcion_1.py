'''1. Obtener existencias: para ello deberá generar una función que cargue
secuencialmente, de tal forma que la intersección de cada fila y cada columna
corresponda a la cantidad de camisetas de un equipo en un depósito. Esto es carga
secuencial.'''

def cargar_existencias (depositos : list, equipos: list)->list:
    "la funcion carga secuencialmente la cantidad de camisetas por deposito"
    matriz = []
    print("------------ carga de equipos por deposito  -------------")
    for i in depositos:
        fila = []
        for j in equipos:
            cantidad = int(input(f"ingrese la cantida de camisetas de {j} para el deposito de {i}: "))
            fila.append(cantidad)
        matriz.append(fila)
    return matriz