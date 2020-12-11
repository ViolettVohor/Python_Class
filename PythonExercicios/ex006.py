n = int(input('Digite um número: '))
print(f'O dobro desse número é \033[7;32;1m{n * 2}\033[m,\nO triplo é \033[41;1m{n * 3}\033[m \nE a raiz quadrada é \033[1;7;30m{n ** (1/2):.2f}\033[m')
