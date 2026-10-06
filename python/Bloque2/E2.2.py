numeros =[3,5,55,88,22,3,5,88]

resultado= []

for elemento in numeros:
    if elemento not in resultado:
        resultado.append(elemento)
        
print(resultado)