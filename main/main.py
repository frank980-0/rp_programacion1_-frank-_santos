from paquetes.funcion_1 import * 
from paquetes.funcion_2 import *
from paquetes.funcion_3 import *
from paquetes.funcion_4 import *
depositos = ["tierra del fuego", "tucuman", "mendoza", "bsas", "misiones" ,"santa fe"]
equipos = ["barcelona", "inter miami", "psg", "manchester city ", "real madrid"]
matriz = []
matriz = cargar_existencias(depositos, equipos)

while True:
    print("""============ MENU =============
        1. obtener existencias 
        2. depositos con mas de 10k de camisetas
        3. equipos con mas de 5k de camisetas
        4. maxima cantidad de camisetas
        9. salir
    """)
    opcion = input("seleccione un opcion (1-9): ")
    if opcion == "1":
        print("---------------- ejercicio 1 ----------------------")
        for i in range(len(depositos)):
            print (f"deposito: {depositos[i]}\n")
            for j in range(len(equipos)):
                print (f" {equipos[j]}: {matriz[i][j]} camisetas\n")
    elif opcion == "2":
        print("---------------- ejercicio 2 ----------------------")
        depositos_mayor_a_10k = calcular_totales (matriz, por_fila = False)
        estima_stock(depositos_mayor_a_10k,depositos, 10000)
    elif opcion ==  "3":
        print("---------------- ejercicio 3 ----------------------")
        equipos_mayor_a_5k = calcular_totales(matriz,por_fila = True)
        estima_stock(equipos_mayor_a_5k, equipos, 5000)
    elif opcion == "4":
        print("---------------- ejercicio 4 ----------------------")
        obtener_maximos(matriz,equipos,depositos)
    elif opcion == "9":
        break