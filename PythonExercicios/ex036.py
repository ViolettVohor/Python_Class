val = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o salário do comprador? R$ '))
ano = int(input('Em quantos anos será pago o empréstimo? '))
pres = val / (ano * 12)
print(f'Para pagar uma casa de R$ {val:.2f} em {ano} anos, a prestação será de R$ {pres:.2f}')
if pres > sal * 0.3:
    print('Empréstimo\033[31;1m não aprovado!')
else:
    print('Empréstimo\033[32;1m aprovado')
