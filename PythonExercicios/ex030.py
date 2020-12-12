num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('Esse número é \033[32;1mPar.')
else:
    print('Esse número é \033[31;1mÍmpar.')
