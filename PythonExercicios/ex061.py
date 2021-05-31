print('Gerador de PA\n' + '-='*7)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1

while cont != 10:
    print(a1, end=' -> ')
    a1 += r
    cont += 1
print('Acabou')
