"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    suma_por_letra = {}

    for line in lines:
        partes = line.strip().split('\t')
        letra = partes[0]
        columna5 = partes[4].split(',')

        # Sumar los valores de la columna 5
        suma_columna5 = sum(int(valor.split(':')[1]) for valor in columna5)

        if letra not in suma_por_letra:
            suma_por_letra[letra] = 0
        suma_por_letra[letra] += suma_columna5

    return suma_por_letra
print(pregunta_12())