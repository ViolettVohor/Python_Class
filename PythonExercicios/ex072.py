extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',\
          'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:  # Repete enquanto o usuário quiser continuar
    while True:  # Repete enquanto o usuário não digitar um número entre 0 e 20
        numero = int(input('Digite um número entre 0 e 20: '))
        if 20 >= numero >= 0:
            break
        print('Tente novamente!', end=' ')
    print(f'Você digitou o número {extenso[numero].capitalize()}')  # Mostra o número que o usuário pediu capitalizado
    while True:  # Repete enquanto o usuário não digitar S ou N
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
