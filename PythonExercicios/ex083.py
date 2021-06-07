dire = 0
esq = 0
exp = input('Digite uma expressão matemática: ')
# noinspection SpellCheckingInspection
exps = []

# noinspection SpellCheckingInspection
for letra in exp:  # Os caracteres da expressão viram elementos na lista exps
    exps.append(letra)
    if letra == '(':  # Conta o número de (
        esq += 1
    elif letra == ')':  # Conta o número de )
        dire += 1

erro = False
for i, char in enumerate(exps):  # Caso tenha algum sinal de operação logo depois de (
    if char == '(' and exps[i+1] in '+-*/^)':
        erro = True  # A expressão está errado
    if char == ')' and exps[i-1] in '+-*/^' and esq != dire:  # Caso tenha alguma sinal de operação logo depois de )
        erro = True  # A expressão está errado

if erro:
    print('Sua expressão está errada!')
else:
    print('Sua expressão está certa!')
