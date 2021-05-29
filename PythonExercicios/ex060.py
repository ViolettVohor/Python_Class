n = int(input('Digite um número: '))
nf = n
fat = 1
while n != 0:
    fat = fat * n
    n -= 1
print(f'O fatorial de {nf} é {fat}')
