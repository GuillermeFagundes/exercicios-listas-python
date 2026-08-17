"""Exercício 2 - Percorrer a lista e exibir os valores maiores que 10."""

numeros = [7, 12, 5, 18, 3, 20]

print("Elementos da lista:")
for numero in numeros:
    print(numero)

print("Elementos maiores que 10:")
for numero in numeros:
    if numero > 10:
        print(numero)
