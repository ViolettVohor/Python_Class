cont = soma = 0

num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma deles é {soma}')
