# E3.2 · Carga iris.csv con DictReader, convierte las medidas a float
# y calcula la media por clase.

# E3.2 · Carga iris.csv con DictReader, convierte las medidas a float
# y calcula la media por clase.

import csv
from pathlib import Path

RUTA = Path(__file__).parent / "iris.csv"
MEDIDAS = ['largo_sep', 'ancho_sep', 'largo_pet', 'ancho_pet']

def obtener_media_columna(filas, columna):
    valores = {}

    # 1. Agrupamos los valores de esa columna concreta por clase
    for fila in filas:
        clase = fila["clase"]

        if clase not in valores:
            valores[clase] = []
        
        # Y convertimos el valor a float directamente aquí
        valores[clase].append(float(fila[columna]))
        
    # 2. Calculamos la media para cada clase dentro de la función
    resultados = {}
    for clase, lista_valores in valores.items():
        media = sum(lista_valores) / len(lista_valores)
        resultados[clase] = media
        
    return resultados


# 3. Abrimos el archivo y cargamos los datos
with open(RUTA, newline="", encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

# 4. Recorremos las columnas y calculamos la media de cada una usando la función
for medida in MEDIDAS:
    medias_por_clase = obtener_media_columna(filas, medida)
    print(f"--- Medias para la columna: {medida} ---")
    for clase, media in medias_por_clase.items():
        print(f"  Clase '{clase}': {media}")
    print()