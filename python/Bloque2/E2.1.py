notas=  [5,4,6,9,1,3,1,3,6,1,3,1,5,3]


media = sum(notas) / len(notas)
maxima = max(notas)
minima = min(notas)

aprobadas = 0
for nota in notas:
    if nota >= 5:
        aprobadas += 1

print(f"Media: {media:.2f}")
print(f"Máxima: {maxima}")
print(f"Mínima: {minima}")
print(f"Aprobadas: {aprobadas}")
