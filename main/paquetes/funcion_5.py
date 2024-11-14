'''5. Cargar ventas: se deberá poder cargar ventas de un determinado producto para un
determinado depósito. Esto es carga distribuida o aleatoria. Al cargarse las ventas
se deben restar los productos vendidos del stock y generar una matriz con la
recaudación que reciba el listado de precios por parámetro, en caso de no recibir un
listado deberá tener un precio de 100 cada producto. Utilizar parámetro opcional.'''

def cargar_ventas (matriz: list, equipos: list, depositos: list, precios)->list: