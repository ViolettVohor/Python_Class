print('-'*30 + '\nSequência de Fibonacci\n' + '-'*30)

n1 = c = 0
n2 = 1
n = int(input('Quantos termos você quer mostrar? '))

print('~'*30)
while c < n:
    c += 1
    if c % 2 != 0:
        print(n1, end=' -> ')
        n1 += n2
    else:
        print(n2, end=' -> ')
        n2 += n1
print('Fim!')
print('~'*30)