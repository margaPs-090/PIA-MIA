# E3.2 · Carga iris.csv con DictReader, convierte las medidas a float
# y calcula la media por clase.
from pathlib import Path

import csv
from pathlib import Path

RUTA = Path(__file__).parent / "iris.csv"

with open(RUTA, newline="", encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

for fila in filas:
    fila["largo_pet"] = float(fila["largo_pet"])

clases = {}
for fila in filas:
    c = fila["clase"]          
    valor = fila["largo_pet"] 
    
    if c not in clases:
        clases[c] = []
    clases[c].append(valor)

for c, valores in clases.items():
    media = sum(valores) / len(valores)
    print(f"Clase '{c}' -> Media: {media}")