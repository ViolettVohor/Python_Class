peso = float(input('Digite o peso da pessoa (Kg): '))
alt = float(input('Digite a altura da pessoa (m): '))
imc = peso / alt ** 2
if imc < 10:
    cat = 'Desnutrição Grau V'
elif imc < 13:
    cat = 'Desnutrição Grau IV '
elif imc < 16:
    cat = 'Desnutrição Grau III'
elif imc < 17:
    cat = 'Desnutrição Grau II'
elif imc < 18.5:
    cat = 'Desnutrição Grau I'
elif imc <= 25:
    cat = 'Normal'
elif imc <= 30:
    cat = 'Pré-Obesidade'
elif imc < 35:
    cat = 'Obesidade Grau I'
elif imc <= 40:
    cat = 'Obesidade Grau II'
else:
    cat = 'Obesidade Grau III'
print(f'O IMC dessa pessoa é \033[35;1m{imc:.1f}\033[m e ela está na categoria \033[36;1m{cat}')
