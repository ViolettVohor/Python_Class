nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
m = (nt1 + nt2) / 2
if m < 5:
    print(f'A média do aluno foi \033[35;1m{m}\033[m e ele foi\033[31;1m Reprovado')
elif m >= 7:
    print(f'A média do aluno foi \033[35;1m{m}\033[m e ele foi\033[32;1m Aprovado')
else:
    print(f'A média do aluno foi \033[35;1m{m}\033[m e ele está de\033[33;1m Recuperção')
