"""Exercício 16 - Exibir matriz 3x3 e calcular suas somas."""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
soma_total = 0

for linha in matriz:
    soma_linha = 0

    for valor in linha:
        print(valor, end=" ")
        soma_total += valor
        soma_linha += valor

    print()
    print("Soma da linha:", soma_linha)

print("Soma total:", soma_total)
