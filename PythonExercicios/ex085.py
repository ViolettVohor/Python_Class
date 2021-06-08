nums = [[], []]
for i in range(1, 8):
    num = int(input(f'Digite o {i}° número: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)

nums[0].sort()
nums[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {nums[0]}')
print(f'Os valores ímpares digitados foram: {nums[1]}')
