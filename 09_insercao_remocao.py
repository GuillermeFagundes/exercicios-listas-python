"""Exercício 9 - Inserir cinco números e remover um valor informado."""

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print("Lista antes:", numeros)
remover = int(input("Qual número deseja remover? "))

if remover in numeros:
    numeros.remove(remover)
else:
    print("Número não encontrado.")

print("Lista depois:", numeros)
