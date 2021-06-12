from datetime import date
ano = date.today().year

pessoa = {'Nome': input('Nome: '),
          'Idade': ano - int(input('Ano de nascimento: ')),  # Recebe o ano de nascimento e calcula a idade
          'CTPS': int(input('Carteira de Trabalho (0 não tem): '))}
if pessoa['CTPS'] != 0:  # Caso a pessoa tenha carteira de trabalho
    pessoa['Contratação'] = int(input('Ano de Contratação: '))  # O dicionário recebe o ano de contratação
    pessoa['Salário'] = float(input('Salário: R$'))  # O salário
    pessoa['Aposentadoria'] = pessoa['Idade'] + (pessoa['Contratação'] - ano + 35)  # E a idade de aposentadoria

print('-='*30)
for k, v in pessoa.items():  # Mostra os dados do dicionário
    print(f'    - {k} tem o valor {v}')
