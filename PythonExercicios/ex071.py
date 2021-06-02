print('='*30)
print(f'{"Caixa Eletrônico":^30}')
print('='*30)

valor = int(input('Informe o valor a ser sacado: R$'))
# cin = vinte = dez = um = 0  # Variáveis que representam a quantidade de cada cédula
ced = 50
totced = 0

while True:
    if valor >= ced:  # Se o valor de saque atual for maior que o valor da cédula
        valor -= ced  # O valor da cédula vai ser subtraido do valor de saque
        totced += 1  # E o total de cédulas desse valor vai receber mais um
    else:  # Se o valor de saque for menor que o valor da cédula
        if totced > 0:  # Cada o total de cédulas desse valor for maior que 0
            print(f'Total de {totced} cédulas de {ced}')  # Será mostrado o total de cédulas

        if ced == 50:  # Se o valor da cédula atual for 50
            ced = 20  # Ele vai receber o valor de 20
        elif ced == 20:   # Se o valor da cédula atual for 20
            ced = 10  # Ele vai receber o valor de 10
        elif ced == 10:  # Se o valor da cédula atual for 10
            ced = 1  # Ele vai receber o valor de 1

        totced = 0  # Reinicia a quantidades de cédulas
        if valor == 0:  # Se o valor de saque zerar, o programa para
            break

'''while True:
    if valor - 50 >= 0:  # Verifica se é possível subtrair 50 do valor atual
        valor -= 50
        cin += 1  # Adicionar mais aos contador de cédulas de 50
    elif valor - 20 >= 0:  # Verifica se é possível subtrair 20 do valor atual
        valor -= 20
        vinte += 1  # Adicionar mais aos contador de cédulas de 20
    elif valor - 10 >= 0:  # Verifica se é possível subtrair 10 do valor atual
        valor -= 10
        dez += 1  # Adicionar mais aos contador de cédulas de 10
    elif valor - 1 >= 0:  # Verifica se é possível subtrair 1 do valor atual
        valor -= 1
        um += 1  # Adicionar mais aos contador de cédulas de 1
    else:
        break
if cin > 0:
    print(f'Total de {cin} cédulas de R$50.')
if vinte > 0:
    print(f'Total de {vinte} cédulas de R$20')
if dez > 0:
    print(f'Total de {dez} cédulas de R$10')
if um > 0:
    print(f'Total de {um} cédulas de R$1')'''

print('='*30)
print(f'{"Volte Sempre!":^30}')
