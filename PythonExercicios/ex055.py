maior = 0
menor = 0

for i in range(1, 6):  # Verifica qual o peso mais pesada e qual o mais leve, em um grupo de 5 pesos
    peso = float(input(f'Digite o {i}° peso: '))
    if i == 1:  # Se for a primeira vez no loop, o menor e o maior recebem o mesmo peso
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é \033[7;1m{maior}kg\033[m '
      f'\nE o menor peso é \033[47;1m{menor}kg\033[m')
