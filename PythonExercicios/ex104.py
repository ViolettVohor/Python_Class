# Não solucionado


def leia_int(txt):
    while True:
        num = input(txt)
        if num == num:
            break
    return num


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
