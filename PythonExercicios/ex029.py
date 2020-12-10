vel = int(input('Qual a velocidade atual do carro em Km/h? '))
if vel > 80:
    print(f'Você excedeu o limite de 80Km/h e foi multado, o valor da multa é R${(vel - 80) * 7:.2f}')
print('Tenha um bom dia! Dirija com cuidado')
