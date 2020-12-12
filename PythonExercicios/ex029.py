vel = int(input('Qual a velocidade atual do carro em Km/h? '))
if vel > 80:
    print(f'Você \033[31;1mexcedeu\033[m o limite de \033[32;1m80Km/h\033[m '
          f'e foi multado, o valor da multa é \033[1;35mR${(vel - 80) * 7:.2f}\033[m')
print('Tenha um bom dia! Dirija com cuidado')
