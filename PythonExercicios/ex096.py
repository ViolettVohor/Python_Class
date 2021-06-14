def area(l, c):
    a = l * c
    print(f'A área do seu terreno de {l:.1f}m X {c:.1f}m é de {a:.1f}m²')


print('-'*40)
print(f'{"Controle de Terrenos":^40}')
print('-'*40)

lar = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(lar, comp)
