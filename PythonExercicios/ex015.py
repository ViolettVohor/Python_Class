dias = int(input('Quantos dias alugados? '))
kilo = float(input('Quantos Km rodados? '))
print(f'O total a pager é de \033[1;4;33mR${dias * 60 + kilo * 0.15:.2f}')
