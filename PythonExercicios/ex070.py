produto_barato = ''
valor_barato = 0
total = 0
cont_custo = 0
cont = 0

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

    if cont == 0:
        produto_barato = nome
        valor_barato = preco
    else:
        if valor_barato > preco:
            valor_barato = preco
            produto_barato = nome
    cont += 1

    if preco > 1000:
        cont_custo += 1

    total += preco

    if continuar == 'N':
        break

print(f'Você gastou R${total}.\n'
      f'Você comprou {cont_custo} produtos que custavam mais que R$1000.\n'
      f'E o produto mais barato foi {produto_barato} que custa R${valor_barato}')
