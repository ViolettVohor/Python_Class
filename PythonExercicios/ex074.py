from random import randint
nums = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)

maior = menor = 0
print(f'Os números sorteador foram:', end=' ')
for pos, num in enumerate(nums):
    print(num, end=' ')
    if pos == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(f'\nO maior número é {maior} e o menor é {menor}')
