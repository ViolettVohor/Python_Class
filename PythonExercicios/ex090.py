aluno = dict()
aluno['Nome'] = input('Nome: ')  # Adiciona o nome do aluno ao dicionário
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))  # Adiciona a média do aluno

if aluno['Média'] >= 7:  # Adiciona a situação do aluno de acordo com a média
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print('-'*30)
for k, v in aluno.items():  # Mostra os dados do dicionário
    print(f'{k} é igual a {v}')
