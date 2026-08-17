"""Exercício 12 - Criar lista sem repetição, sem usar set()."""

numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10]
sem_repeticao = []

for numero in numeros:
    if numero not in sem_repeticao:
        sem_repeticao.append(numero)

print("Lista sem repetição:", sem_repeticao)
