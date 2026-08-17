"""Exercício 6 - Contar números pares e ímpares."""

numeros = [5, 8, 12, 7, 3, 10, 4, 9, 15, 2]
pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Ímpares:", impares)
