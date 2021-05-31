resp = 'S'
num = soma = cont = menor = maior = 0

while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1

    if cont > 1:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    else:
        maior = menor = num

    resp = (input('Deseja continuar? [S/N] ')).strip()[0]

print(f'Você digitou {cont} números e a média desses números é {soma / cont},'
      f'\no maior número é {maior} e o menor é {menor}')
