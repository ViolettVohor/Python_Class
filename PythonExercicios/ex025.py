n = input('Digite seu nome completo: ').strip()
print(f'Em seu nome tem Silva? \033[35m{"silva" in n.lower()}')
