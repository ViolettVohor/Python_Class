n = input('Digite seu nome completo: ').strip()
color = {'l': '\033[m', 'v': '\033[1;32m'}
print(f'Seu nome em Maiúsculo é {color["v"]}{n.upper()}{color["l"]}')
print(f'Seu nome em Minúsculo é {color["v"]}{n.lower()}{color["l"]}')
print(f'Seu nome ao todo tem {color["v"]}{len(n.replace(" ", ""))}{color["l"]} letras')
# print(f'Seu nome ao todo tem {color["v"]}{len(n) - n.count(" ")}{color["l"]} letras')
print(f'Seu primero nome é {color["v"]}{n.split()[0]}{color["l"]}'
      f' e ele tem {color["v"]}{len(n.split()[0])}{color["l"]} letras')
# print(f'Seu primero nome é {color["v"]}{n.split()[0]}{color["l"]} '
#       f'e ele tem {color["v"]}{n.find(" ")}{color["l"]} letras')
