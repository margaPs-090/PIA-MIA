# Conversor de unidades: pide grados Celsius y muestra
# Fahrenheit y Kelvin con 2 decimales.

celsius = float(input("Introduce la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

# Mostramos los resultados formateados a 2 decimales
print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")
print(f"{celsius} °C equivalen a {kelvin:.2f} K")
