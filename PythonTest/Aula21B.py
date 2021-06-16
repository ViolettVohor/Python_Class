def fatorial(num=1):
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    return fat


n = int(input('Digite um número: '))
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print(f'Os resultados são {f1}, {f2}, {f3}')
