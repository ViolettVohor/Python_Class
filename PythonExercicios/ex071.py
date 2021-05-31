print('='*30)
print(f'{"Caixa Eletrônico":^30}')
print('='*30)

valor = int(input('Informe o valor a ser sacado: R$'))
cin = vinte = dez = um = 0

while True:
    if valor - 50 >= 0:
        valor -= 50
        cin += 1
    elif valor - 20 >= 0:
        valor -= 20
        vinte += 1
    elif valor - 10 >= 0:
        valor -= 10
        dez += 1
    elif valor - 1 >= 0:
        valor -= 1
        um += 1
    else:
        break
if cin > 0:
    print(f'Total de {cin} cédulas de R$50.')
if vinte > 0:
    print(f'Total de {vinte} cédulas de R$20')
if dez > 0:
    print(f'Total de {dez} cédulas de R$10')
if um > 0:
    print(f'Total de {um} cédulas de R$1')

print('='*30)
print(f'{"Volte Sempre!":^30}')
