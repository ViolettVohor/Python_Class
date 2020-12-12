km = float(input('Qual a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de \033[33;1m{km}Km\033[m')
# if km <= 200:
#     preco = km * 0.5
# else:
#     preco = km * 0.45
preco = km * 0.5 if km <= 200 else km * 0.45
print(f'O valor da passagem é \033[32;1mR${preco:.2f}')
