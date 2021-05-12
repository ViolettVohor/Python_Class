n = int(input('Digite um número inteiro: '))
p = 0
for i in range(n, 0, -1):
    if n % i == 0:
        p += 1
if p == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')
