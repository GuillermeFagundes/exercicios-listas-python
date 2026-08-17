"""Exercício 8 - Informar a posição de um nome sem usar index()."""

nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
pesquisa = input("Informe um nome: ")
posicao = -1

for i in range(len(nomes)):
    if nomes[i] == pesquisa:
        posicao = i

if posicao != -1:
    print(f"{pesquisa} está na posição {posicao}.")
else:
    print("Nome não encontrado.")
