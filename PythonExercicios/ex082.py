val = []
while True:
    val.append(int(input('Digite um número: ')))
    while True:  # Caso o usuário não digite S ou N, é feita novamente a pergunta
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break

par = list()
impar = []
for v in val:
    if v % 2 == 0:  # Caso o valor for par é adicionado a lista par
        par.append(v)
    else:  # Mas se for ímpar é adicionado a lista impar
        impar.append(v)

print('-='*20)
print(f'Você digitou os números: {val}')
print(f'Entre eles, esses eram os pares: {par}')
print(f'E esses os ímpares: {impar}')
