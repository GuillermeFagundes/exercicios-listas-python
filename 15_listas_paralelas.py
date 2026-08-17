"""Exercício 15 - Relacionar alunos e notas em listas paralelas."""

alunos = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
notas = [8.0, 5.5, 7.5, 4.0, 9.0]

for i in range(len(alunos)):
    if notas[i] >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"{alunos[i]} - Nota: {notas[i]} - {situacao}")
