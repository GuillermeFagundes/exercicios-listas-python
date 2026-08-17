"""Exercício 18 - Contar manualmente a frequência dos elementos."""

numeros = [2, 3, 2, 5, 3, 2]
verificados = []

for numero in numeros:
    if numero not in verificados:
        quantidade = 0

        for valor in numeros:
            if valor == numero:
                quantidade += 1

        print(f"{numero} aparece {quantidade} vez(es).")
        verificados.append(numero)
