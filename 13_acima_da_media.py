"""Exercício 13 - Exibir os valores acima da média."""

numeros = []

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)
print(f"Média: {media:.2f}")
print("Valores acima da média:")

for numero in numeros:
    if numero > media:
        print(numero)
