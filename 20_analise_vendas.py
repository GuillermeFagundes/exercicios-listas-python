"""Exercício 20 - Analisar uma lista de vendas diárias."""

vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]
total = 0

for venda in vendas:
    total += venda

media = total / len(vendas)
maior = vendas[0]
menor = vendas[0]

for venda in vendas:
    if venda > maior:
        maior = venda
    if venda < menor:
        menor = venda

dias_acima = 0
for venda in vendas:
    if venda > media:
        dias_acima += 1

percentual = (dias_acima / len(vendas)) * 100

print(f"Total vendido: R$ {total:.2f}")
print(f"Média diária: R$ {media:.2f}")
print(f"Maior venda: R$ {maior:.2f}")
print(f"Menor venda: R$ {menor:.2f}")
print(f"Dias acima da média: {dias_acima}")
print(f"Percentual acima da média: {percentual:.2f}%")
