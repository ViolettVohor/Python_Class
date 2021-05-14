s = 0
c = 0
for i in range(1, 500, 2):  # Conta de 1 até 500, verifica quais números são ímpares e multiplos de três e soma eles
    if i % 3 == 0:
        s += i
        c += 1
print(f'\033[34;1mA soma dos números ímpares que são multiplos de três'
      f' e estão entre 1 e 500, é\033[m \033[41;7;1m{s}\033[m\033[34;1m, '
      f'e existem \033[32;1m{c}\033[34;1m deles entre 1 e 500\033[m')
