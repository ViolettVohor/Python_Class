def leia_int(txt):
    while True:
        num = input(txt)
        if num.isdigit():
            break
        else:
            print('\033[31;1mERRO! Digite um número.\033[m')
    return num


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
