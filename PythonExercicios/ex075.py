nums = int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),\
       int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: '))
print(f'Você digitou os valores: {nums}')

noves = par = 0
for num in nums:
    if num == 9:
        noves += 1
    if num % 2 == 0:
        par += 1
print(f'Apareceu {noves} vezes o número nove')
try:
    print(f'O valor 3 foi digitado na {nums.index(3) + 1}° posição')
except ValueError:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Você digitou {par} números pares')
