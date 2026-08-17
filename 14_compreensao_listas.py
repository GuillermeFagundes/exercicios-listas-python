"""Exercício 14 - Criar listas usando list comprehension."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = [numero ** 2 for numero in numeros]
pares = [numero for numero in numeros if numero % 2 == 0]
maiores_5 = [numero for numero in numeros if numero > 5]

print("Quadrados:", quadrados)
print("Pares:", pares)
print("Maiores que 5:", maiores_5)
