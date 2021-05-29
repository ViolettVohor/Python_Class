a1 = int(input('Digite o 1° termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
an = a1

while an != a1 + 10 * r:
    print(an, end=' -> ')
    an += r
print('Acabou')
