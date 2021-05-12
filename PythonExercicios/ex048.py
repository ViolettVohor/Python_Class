s = 0
for i in range(1, 500):  # Conta de 1 até 500, verifica quais números são ímpares e multiplos de três e soma eles
    if i % 2 != 0 and i % 3 == 0:
        s += i
print(f'\033[34;1mA soma dos números ímpares que são multiplos de três'
      f' e estão entre 1 e 500, é\033[m \033[41;7;1m{s}\033[m')
