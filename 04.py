quantidade_macas = int(input('Quantas maçãs você quer comprar?\nQuantidade: '))
preco = 0.30 if quantidade_macas < 12 else 0.25

valor_total = quantidade_macas * preco

print(f'Preço: {valor_total}')
