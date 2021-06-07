valores = list()  # Cria uma lista vazia
# valores = []  # Também cria uma lista vazia
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))  # Adiciona os valores digitados pelo usuário a lista

for i, v in enumerate(valores):
    print(f'na posição {i} encontrei o valor {v}...')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a  # Linka a lista 'a' a lista 'b'
c = a[:]  # Cria uma copia da lista 'a', que é a lista 'c'
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
