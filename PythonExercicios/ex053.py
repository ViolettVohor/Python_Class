frase = input('Digite uma frase: ').lower().strip()  # Pede pro usuário digitar uma frase

frase_cut = frase.split()  # Divide essa frase de acordo com os espaços
frase_filtro = ''.join(frase_cut)  # Junta a frase invertida que foi divida para vira apenas uma palavra
frase_inv = frase_filtro[::-1]  # Inverte a frase, serve apenas para Python

'''
inverso = ''
for letra in range(len(frase_filtro) - 1, -1, -1):
    inverso += frase_filtro[letra]

for i in range(0, len(frase_cut_inv)):  
    frase_inv_filtro += frase_cut_inv[i]
for i in range(0, len(frase_cut)):  
    frase_filtro += frase_cut[i]
'''

print(f'O inverso de {frase_filtro} é {frase_inv}')
if frase_inv == frase_filtro:  # Verifica se a frase normal e a invertida são iguais, elas estão sem os espaços
    print('Essa frase é \033[32;1mum palíndromo')
else:
    print('Essa frase\033[31;1m não é um palíndromo')
