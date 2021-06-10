nums = [[], []]  # Lista com duas listas internas
for i in range(1, 8):
    num = int(input(f'Digite o {i}° número: '))
    if num % 2 == 0:  # Caso num for par
        nums[0].append(num)  # Adiciona o valor de 'num' dentro da primeira lista de 'nums'
    else:  # Caso num for ímpar
        nums[1].append(num)  # Adiciona o valor de 'num' dentro da segunda lista de 'nums'

nums[0].sort()  # Organiza os valores da lista par
nums[1].sort()  # Organiza os valores da lista ímpar
print('-='*30)
print(f'Os valores pares digitados foram: {nums[0]}')  # Mostra os valores da lista par (nums[0])
print(f'Os valores ímpares digitados foram: {nums[1]}')  # Mostra os valores da lista ímpar (nums[1])
