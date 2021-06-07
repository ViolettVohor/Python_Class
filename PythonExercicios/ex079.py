val = list()
while True:
    inserir = int(input('Digite um valor: '))
    if inserir in val:  # Caso o valor digitado já tenha sido inserido ele não será inserido novamente
        print('Esse valor já foi inserido.')
    else:
        print('Valor adicionado com sucesso.')
        val.append(inserir)

    while True:  # Caso o usuário não digite S ou N, será perguntado novamente
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break

val.sort()  # Organiza os elementos em ordem crescente
print('-='*20)
print(f'Você digitou os valores: {val}')  # Mostra os elementos
