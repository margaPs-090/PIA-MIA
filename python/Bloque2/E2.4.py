texto = input("Introduce un texto: ")

texto = texto.lower()

palabras = texto.split()

frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

ordenadas = sorted(frecuencia.items())

print("\nTop 5 palabras:")