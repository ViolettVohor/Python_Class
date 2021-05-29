a1 = int(input('Digite o 1° termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
an = a1
n = 10
c = 0

while an < a1 + n * r:
    print(an, end=' -> ')
    an += r
    c += 1
    if c == n:
        n += int(input('\nVocê quer que repita mais quantas vezes? '))
print('Acabou')
