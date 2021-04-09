lar = float(input('Qual a largura da parede, em metros? '))
alt = float(input('Qual a altura da parede, em metros? '))
# Pede ao usuário que digite as medida da parede
print(f'Sua parede tem \033[31;1m{lar*alt:.1f}m²\033[m e você precisa de \033[36;1m{lar*alt/2:.1f}\033[m Litros de tinta')
