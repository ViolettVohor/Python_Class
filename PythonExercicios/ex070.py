produto_barato = ''  # Nome do produto mais barato
valor_barato = 0  # Valor do produto mais barato
total = 0  # Total da compra
cont_custo = 0  # Quantos produtos custam mais de 1000
index = 0  # index dos produtos

print('-'*30)
print(f'{"SUPERMERCADO MAIS":^30}')
print('-'*30)
while True:
    nome = input('Qual o nome do produto? ')
    preco = int(input('Qual o valor? R$'))

    while True:
        continuar = input('Deseja continuar? [S/N] ').upper().split()[0]
        if continuar in 'SN':
            break
    print('-'*30)

    index += 1
    if index == 1:  # Se o index = 1 então
        produto_barato = nome
        valor_barato = preco
    else:  # Se não, verifica se o valor é menor que o menor valor anterior
        if valor_barato > preco:
            valor_barato = preco
            produto_barato = nome

    if preco > 1000:  # Se o valor maior que 1000, cont_custo recebe mais um
        cont_custo += 1

    total += preco

    if continuar == 'N':  # Se continuar = N então encerra o laço
        break

print(f'Você gastou R${total}.\n'
      f'Você comprou {cont_custo} produtos que custavam mais que R$1000.\n'
      f'E o produto mais barato foi {produto_barato} que custa R${valor_barato}')
