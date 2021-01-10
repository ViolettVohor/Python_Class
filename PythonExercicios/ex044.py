print(f'{" Lojas Lojas ":=^40}')
pre = float(input('Digite o valor do produto: R$ '))
con = int(input('1 - À vista em Dinheiro/Cheque '
                '\n2 - À vista no Cartão '
                '\n3 - em até 2x no Cartão '
                '\n4 - 3x ou mais no Cartão'
                '\nSelecione a condição de pagamento: '))
if con == 1 or con == 2 or con == 3 or con == 4:
    if con == 1:
        pre = pre * 0.9
        forma = 'À vista em Dinheiro/Cheque'
    elif con == 2:
        pre = pre * 0.95
        forma = 'À vista no Cartão'
    elif con == 3:
        print(f'Você irá pagar em 2x de R$ {(pre/2):.2f} SEM JUROS')
        forma = 'em até 2x no Cartão'
    elif con == 4:
        pre = pre * 1.2
        parc = int(input('Quantas parcelas? '))
        print(f'Você irá pagar em {parc}x de R$ {(pre/parc):.2f} COM JUROS')
        forma = '3x ou mais no Cartão'
    # noinspection PyUnboundLocalVariable
    print(f'Você escolheu \033[35;1m{forma}\033[m e o total à ser pago é \033[36;1mR${pre:.2f}')
else:
    print('\033[31;1mOpção inválida de pagamento. Tente Novamente')
