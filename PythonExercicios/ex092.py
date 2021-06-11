from datetime import date
ano = date.today().year

pessoa = {'Nome': input('Nome: '),
          'Idade': ano - int(input('Ano de nascimento: ')),
          'CTPS': int(input('Carteira de Trabalho (0 não tem): '))}
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + 35

print('-='*30)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
