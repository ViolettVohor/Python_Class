num = 0
resp = 'S'
soma = 0
cont = 0
menor = 0
maior = 0

while resp == 'S':
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

    resp = (input('Deseja continuar? [S/N] ')).upper()

print(f'A média desses números é {soma / cont}, o maior número é {maior} e o menor é {menor}')
