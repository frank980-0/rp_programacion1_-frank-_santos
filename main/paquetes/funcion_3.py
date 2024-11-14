'''3. Mostrar equipos que hay en stock más de 5.000 camisetas.'''
from paquetes.funcion_2 import *
'''esta funcion permite asignar un limite para poder solo mostrar del limite permitido
esta vinculada con la funcion 2'''
def estima_stock (totales: list,nombre: list,limite:int)-> list:
    for i in range (len(totales)):
        if totales[i] > limite:
            print(f"{nombre[i]} tiene {totales[i]} camisetas en total")