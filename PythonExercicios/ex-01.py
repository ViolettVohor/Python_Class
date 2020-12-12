preco = float(input('Digite o valor do produto: R$'))
print(f'O valor desse produto à vista, com 15% de desconto, é \033[1;37mR${preco * 0.85:.2f}\033[m')
print(f'E a prazo, com aumento de 10%, é \033[1;36mR${preco * 1.1:.2f}')
