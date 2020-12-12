val = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário do comprador? R$'))
ano = int(input('Em quantos anos será pago o empréstimo? '))
pres = val / (ano * 12)
if pres > sal * 0.3:
    print('Empréstimo\033[31;1m não aprovado!')
else:
    print('Empréstimo\033[32;1m aprovado')
