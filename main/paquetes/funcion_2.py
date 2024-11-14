'''2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.'''
def calcular_totales (matriz: list, por_fila = True)-> list:
    '''esta funcion calcula la cantidad totales de las cantidades en los depositos 
    y la cantidad total de las camisertas por equipo'''
    totales = []
    if por_fila:  # suma por columnas que serian los equipos
        for j in range(len(matriz[0])):
            total = 0
            for i in range(len(matriz)):
                total += matriz [i][j]
        totales.append(total)
    else: # sumar las filas que son los depositos
        for fila in matriz:
            total = 0
            for cantidad in fila:
                total += cantidad
            totales.append(total)
    return totales