"""Exercício 17 - Encontrar o segundo maior distinto sem sort()."""

numeros = [10, 25, 8, 40, 17, 40, 30]
maior = None
segundo_maior = None

for numero in numeros:
    if maior is None or numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero != maior and (segundo_maior is None or numero > segundo_maior):
        segundo_maior = numero

print("Maior:", maior)
print("Segundo maior:", segundo_maior)
