from random import choice
n1 = input('Digite o Nome do primeiro aluno: ')
n2 = input('Digite o Nome do segundo aluno: ')
n3 = input('Digite o Nome do terceito aluno: ')
n4 = input('Digite o Nome do quarto aluno: ')
alunos = [n1, n2, n3, n4]
print(f'O aluno que vai apagar o quadro é \033[34;1m{choice(alunos)}')
