from random import randint
nums = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
# tupla com 5 números aleatórios

# maior = menor = 0
print(f'Os números sorteador foram:', end=' ')
for pos, num in enumerate(nums):  # Mostra os 5 elementos da tupla 'nums'
    print(num, end=' ')
    '''if pos == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num'''
print(f'\nO maior valor foi {max(nums)}')  # Mostra o maior elemento dentro da tupla
print(f'O menor valor foi {min(nums)}')  # Mostra o menor elemento dentro da tupla
# print(f'\nO maior número é {maior} e o menor é {menor}')
