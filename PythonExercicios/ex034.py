sal = float(input('Digite seu salário: R$'))
if sal <= 1250:
    print(f'Seu novo salário é {sal * 1.15:.2f}')
else:
    print(f'Seu novo salário é {sal * 1.10:.2f}')
