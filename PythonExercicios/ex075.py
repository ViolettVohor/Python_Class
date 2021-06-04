nums = int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),\
       int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: '))
print(f'\nVocê digitou os valores: {nums}')

print(f'Apareceu {nums.count(9)} vezes o número nove')

if 3 in nums:  # try:
    # Mostra a posição do 3 na tupla, caso ele exista na tupla
    print(f'O valor 3 foi digitado na {nums.index(3) + 1}° posição')
else:  # except ValueError:
    # Informa que não existe um 3 na tupla
    print('O valor 3 não foi digitado em nenhuma posição')

par = 0
for num in nums:  # Conta a quantidade de números pares
    if num % 2 == 0:
        par += 1
print(f'Você digitou {par} números pares que são', end=' ')
for n in nums:  # Mostra os números pares
    if n % 2 == 0:
        print(n, end=' ')
