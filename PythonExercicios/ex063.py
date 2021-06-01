print('-'*30 + '\nSequência de Fibonacci\n' + '-'*30)

n1 = index = 0  # Primeiro valor da Sequência e o index dos valores
n2 = 1  # Segundo valor da Sequência
termos = int(input('Quantos termos você quer mostrar? '))

print('~'*30)
while index < termos:
    index += 1
    if index % 2 != 0:
        print(n1, end=' -> ')
        n1 += n2  # O primeiro valor recebe a soma dele com o segundo valor
    else:
        print(n2, end=' -> ')
        n2 += n1  # O segundo valor recebe a soma dele com o primeiro valor
print('Fim!')
print('~'*30)
