peso = float(input('Digite o peso da pessoa: '))
alt = float(input('Digite a altura da pessoa: '))
imc = peso / alt ** 2
if imc < 18.5:
    cat = 'Abaixo do peso'
elif imc <= 25:
    cat = 'Peso Ideal'
elif imc <= 30:
    cat = 'Sobrepeso'
elif imc <= 40:
    cat = 'Obesidade'
else:
    cat = 'Obesidade Mórbida'
print(f'O IMC dessa pessoa é \033[35;1m{imc:.1f}\033[m e ela está na categoria \033[36;1m{cat}')
