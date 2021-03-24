n = int(input('Digite um número: '))
# Pede que o usuário digite um número e armazena na variável

print(f'O dobro desse número é \033[7;32;1m{n * 2}\033[m,'
      f'\nO triplo é \033[41;1m{n * 3}\033[m \nE a raiz quadrada é \033[1;7;30m{n ** (1/2):.2f}\033[m')
# Mostra o dobro, o triplo e a raiz quadrada do número digitado
# Mostra o dobro em negrito (1), ele teria a fonte verde (32), mas o fundo e a fonte estão invertidas (7)
# Triplo: negrito (1), fundo vermelho (41)
# Raiz: negrito (1), a fonte seria branca (30), mas o fundo e a fonte estão invertidos (7)
