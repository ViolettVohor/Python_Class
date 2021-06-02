while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if n < 0:  # Mostra a tabuada enquanto o usuário não digitar um valor negativo
        break
    for i in range(0, 11):  # Quando o progressão é de apenas 1, o 1 pode ser omitido
        print(f'{n} X {i} = {n*i}')
    print('-'*35)
print('Tabuada Encerrada. Volte Sempre!')
