from random import shuffle
n1 = input('Digite o Nome do Primeiro aluno: ')
n2 = input('Digite o Nome do Segundo aluno: ')
n3 = input('Digite o Nome do Terceiro aluno: ')
n4 = input('Digite o Nome do Quarto aluno: ')
al = [n1, n2, n3, n4]
shuffle(al)
print(f'A ordem dos alunos é \033[7;30;1m {al[0]} \033[m, \033[37;1m{al[1]}\033[m, \033[1;34m{al[2]}\033[m, \033[1;46m {al[3]} \033[m')
# print(f'A ordem dos alunos é {al}')
