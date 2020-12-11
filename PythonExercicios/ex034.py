sal = float(input('Digite seu salário: R$'))
if sal <= 1250:
    novo = sal * 1.15
else:
    novo = sal * 1.1
print(f'Seu antigo salário era {sal} e o seu novo salário é {novo:.2f}')
