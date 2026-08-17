"""Exercício 4 - Calcular a média das notas."""

notas = [7.5, 8.0, 6.0, 9.5, 5.5]
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media:.2f}")
