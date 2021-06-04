print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)

produtos = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,\
    'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9

for pos, pro in enumerate(produtos):  # for pos in range(0, len(produtos))
    if pos % 2 == 0:  # Caso o index for par então mostra o elemento com essa formatação
        print(f'{pro:.<40}', end='')
    else:  # Se for ímpar mostra com essa formatação
        print(f'R${pro:>8.2f}')

print('-'*50)
