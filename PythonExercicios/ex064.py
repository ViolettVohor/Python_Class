cont = -1
num = 0
soma = 0

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número: '))
print(f'Você digitou {cont} números e a soma deles é {soma}')
