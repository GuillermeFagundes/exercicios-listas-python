"""Exercício 19 - Controle de estoque com listas paralelas."""

produtos = ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]
quantidades = [12, 25, 4, 3, 8]

pesquisa = input("Qual produto deseja consultar? ")
encontrado = False

for i in range(len(produtos)):
    if produtos[i] == pesquisa:
        print(f"{produtos[i]} possui {quantidades[i]} unidades.")
        encontrado = True

if not encontrado:
    print("Produto não encontrado.")

produto_alterar = input("Qual produto deseja alterar? ")

for i in range(len(produtos)):
    if produtos[i] == produto_alterar:
        nova_quantidade = int(input("Informe a nova quantidade: "))
        quantidades[i] = nova_quantidade

print("Produtos com estoque inferior a 5:")
for i in range(len(produtos)):
    if quantidades[i] < 5:
        print(produtos[i], "-", quantidades[i])

maior_quantidade = quantidades[0]
produto_maior = produtos[0]

for i in range(len(produtos)):
    if quantidades[i] > maior_quantidade:
        maior_quantidade = quantidades[i]
        produto_maior = produtos[i]

print(
    f"Produto com maior estoque: {produto_maior} "
    f"com {maior_quantidade} unidades."
)
