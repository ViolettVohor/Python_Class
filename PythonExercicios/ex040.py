nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
m = (nt1 + nt2) / 2
if m < 5:
    print('O aluno foi \033[31;1mReprovado')
elif m >= 7:
    print('O aluno foi \033[32;1mAprovado')
else:
    print('O aluno está de \033[33;1mRecuperção')
