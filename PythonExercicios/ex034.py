sal = float(input('Digite seu salário: R$'))
if sal <= 1250:
    novo = sal * 1.15
else:
    novo = sal * 1.1
print(f'Seu antigo salário era \033[1;37m{sal}\033[m e o seu novo salário é \033[36;1m{novo:.2f}')
