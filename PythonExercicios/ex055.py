maior = 0
menor = 89574395305703

for i in range(0, 5):  # Verifica quem é a pessoa mais leve e a mais pesada, em um grupo de 5 pessoas
    peso = float(input('Digite o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'A pessoa mais pesada pesa \033[7;1m{maior}kg\033[m e a mais leva pesa \033[47;1m{menor}kg\033[m')
