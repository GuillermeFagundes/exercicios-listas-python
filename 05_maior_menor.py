"""Exercício 5 - Encontrar maior e menor sem max() e min()."""

numeros = [15, 8, 23, 4, 17, 10]
maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("Maior:", maior)
print("Menor:", menor)
