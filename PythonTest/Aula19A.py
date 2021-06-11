pessoas = {'nome': 'Matheus',
           'sexo': 'M',
           'idade': '17'}

print(pessoas['sexo'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

del pessoas['sexo']
pessoas['nome'] = 'Oliver'
pessoas['idade'] = 25
pessoas['peso'] = 70.5
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
