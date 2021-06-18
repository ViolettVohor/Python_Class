pessoas = {'nome': 'Matheus',
           'sexo': 'M',
           'idade': '17'}

print(pessoas['sexo'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())  # Mostra as chaves ("indexes") do dicionário
print(pessoas.values())  # Mostra os valores do dicionário
print(pessoas.items())  # Mostra as chaves e os valores do dicionário

del pessoas['sexo']  # Deleta a chave 'sexo' e o seu valor
pessoas['nome'] = 'Oliver'
pessoas['idade'] = 25
pessoas['peso'] = 70.5
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')

# Exercício 90 - 95
