# Clasificador de notas: pide una nota, valida el rango 0-10 y
#  muestra la calificación.

nota = float(input("Introduce una nota (0-10): "))

if nota < 0 or nota > 10:
    print("Nota no válida")
elif nota < 5:
    print("Suspenso")
elif nota < 6:
    print("Aprobado")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")