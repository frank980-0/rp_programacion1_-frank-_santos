'''4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
encuentra.'''
'''esta funcion permite calcular la cantidad maxima de camisetas de cada equipo y muestra en que
deposito se encuentra'''
def obtener_maximos (matriz : list, equipos:list, depositos: list)-> list:
    for j in range (len(matriz[0])):
        max_cantidad = matriz[0][j]
        depositos_maximo = depositos[0]
        for i in range (1, len(matriz)):
            if matriz[i][j] > max_cantidad:
                max_cantidad = matriz[i][j]
                depositos_maximo = depositos [i]
        print (f"el equipo {equipos[j]} tiene {max_cantidad} camisetas en el deposito {depositos_maximo}")        