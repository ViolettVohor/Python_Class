s = 0
c = 0
for i in range(1, 7):  # Pede para o usuário digitar seis números inteiros e soma aqueles que forem par
    n = int(input(f'Digite o {i}° valor: '))
    if n % 2 == 0:
        s += n
        c += 1
print(f'\n\033[7;1mVocê digitou \033[43;1m{c}\033[m\033[7;1m números pares e a soma deles é \033[46;7;1m{s}\033[m')
