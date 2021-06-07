cont = 0
val = list()
while True:
    val.append(int(input('Digite um número: ')))
    cont += 1
    while True:  # Caso o usuário não digite S ou N, é feita novamente a pergunta
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break

print('-='*20)
print(f'Você digitou {cont} números')
if 5 in val:  # Caso o 5 tenha sido digitado, mostra as posições
    print('O número 5 foi digitado nas posições:', end=' ')
    for i, v in enumerate(val):
        if v == 5:
            print(i, end='...')
else:
    print('O número 5 não foi digitado.')
val.sort(reverse=True)  # Reordena os número em ordem decrescente
print(f'\nOs números em ordem decrescente: {val}')
