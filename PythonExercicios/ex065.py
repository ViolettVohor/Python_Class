resp = 'S'
num = soma = cont = menor = maior = 0

while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num  # Soma todos os números digitados
    cont += 1  # Conta quantos número foram digitados

    if cont > 1:  # Se não for o primeiro número, então verifica se é o maior ou menor número até agora
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    else:  # Se for o primeiro número, então ele é o maior e o menor número
        maior = menor = num

    resp = (input('Deseja continuar? [S/N] ')).strip()[0]

print(f'Você digitou {cont} números e a média desses números é {soma / cont},'
      f'\no maior número é {maior} e o menor é {menor}')
