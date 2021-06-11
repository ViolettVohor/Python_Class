brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Paraíba', 'sigla': 'PB'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])

estado = dict()
pais = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    pais.append(estado.copy())  # Cria uma copia, assim os valores da lista 'pais', não ficam vínculados ao dicionário
for e in pais:
    for v in e.values():
        print(v, end=' ')
    print()
