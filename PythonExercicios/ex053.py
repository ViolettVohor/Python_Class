frase = input('Digite uma frase: ').lower()  # Pede pro usuário digitar uma frase
frase_cut = frase.split(' ')  # Divide essa frase de acordo com os espaços
frase_inv = frase[::-1]  # Inverte a frase
frase_cut_inv = frase_inv.split(' ')  # Divida a frase invertida de acordo com os espaços

p = 0
frase_inv_filtro = ''
frase_filtro = ''

for i in range(0, len(frase_cut_inv)):  # Junta a frase invertida que foi divida para vira apenas uma palavra
    frase_inv_filtro += frase_cut_inv[i]
for i in range(0, len(frase_cut)):  # Junta a frase que foi divida para vira apenas uma palavra
    frase_filtro += frase_cut[i]

if frase_inv_filtro == frase_filtro:  # Verifica se a frase normal e a invertida são iguais, elas estão sem os espaços
    print('Essa frase é \033[32;1mum palíndromo')
else:
    print('Essa frase\033[31;1m não é um palíndromo')
