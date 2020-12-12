c = float(input('Digite a temperatura em Celsius: '))
print(f'A temperatura \033[34;1m{c}°C\033[m vale \033[31;1m{c * 1.8 + 32}°F\033[m e \033[32;1m{c + 273.15}K')
