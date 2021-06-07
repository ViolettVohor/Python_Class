valores = []
for c in range(0, 5):  # Armazena 5 valores digitados pelo usuário na lista valores
    valores.append(int(input(f'Digite o {c + 1}° valor: ')))

print('=-'*30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor é {max(valores)} e ele está nas posições', end=' ')
for i, v in enumerate(valores):
    if max(valores) == v:
        print(i + 1, end='...')
# Mostra o maior valor e suas posições, caso tenha aparecido em mais de uma

print(f'\nO menor valor foi {min(valores)} e ele está na posição', end=' ')
for i, v in enumerate(valores):
    if min(valores) == v:
        print(i + 1, end='...')
# Mostra o menor valor e suas posições, caso tenha aparecido em mais de uma
