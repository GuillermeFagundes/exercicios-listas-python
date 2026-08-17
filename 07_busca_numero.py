"""Exercício 7 - Buscar um número sem usar index()."""

numeros = []

for i in range(8):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

pesquisa = int(input("Qual número deseja pesquisar? "))
encontrado = False

for numero in numeros:
    if numero == pesquisa:
        encontrado = True

if encontrado:
    print("O número está na lista.")
else:
    print("O número não está na lista.")
