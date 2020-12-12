num = int(input('Digite um número inteiro: '))
choose = int(input('Qual a base de conversão?\n1 para binário\n2 para octal\n3 para hexadecimal '))
if choose == 1:
    print(f'\033[37;1m{num}\033[m convertido para binário vale \033[31;1m{num:b}')
elif choose == 2:
    print(f'\033[37;1m{num}\033[m convertido para octal vale \033[32;1m{num:o}')
elif choose == 3:
    hex = f'{num:x}'
    print(f'\033[37;1m{num}\033[m convertido hexadecimal vale \033[33;1m{hex.upper()}')
else:
    print('Digite um número\033[36;1m correspondente\033[m a uma base')
