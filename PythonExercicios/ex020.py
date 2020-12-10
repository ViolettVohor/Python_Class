from random import shuffle
n1 = input('Digite o Nome do Primeiro aluno: ')
n2 = input('Digite o Nome do Segundo aluno: ')
n3 = input('Digite o Nome do Terceiro aluno: ')
n4 = input('Digite o Nome do Quarto aluno: ')
al = [n1, n2, n3, n4]
shuffle(al)
print(f'A ordem dos alunos é {al[0]}, {al[1]}, {al[2]}, {al[3]}')
# print(f'A ordem dos alunos é {al}')
