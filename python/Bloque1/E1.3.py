# Tabla de multiplicar con formato alineado usando f-strings
numero = int(input("Introduce un número: "))

for i in range(1, 11):
    print(f"{numero:2} x {i:2} = {numero*i:3}")