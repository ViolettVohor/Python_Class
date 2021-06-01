soma = cont = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:  # Se o usuário digitar 999 o laço para
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma deles é {soma}')
