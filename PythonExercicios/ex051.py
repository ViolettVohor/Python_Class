print('='*30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('='*30)

a1 = int(input('Digite um número: '))
r = int(input('Digite a razão da Progressão Aritmética: '))


for i in range(a1, a1 + 10 * r, r):
    # Calcula o décimo termo da PA e mostra os 10 primeros termos
    print(f'\033[1;35m{i}', end=' -> ')
print('Acabou!')
