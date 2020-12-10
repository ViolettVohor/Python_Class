# nome = input('Qual seu nome? ')
# if 'Oliver' in nome:
#    print('Que nome lindo você tem!')
# else:
#    print('Seu nome é tão normal')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média é {:.1f}'.format(m))
print('Parabéns, você foi Aprovado!' if m >= 6 else 'Você foi Reprovado! Se esforce mais')
# if m < 6:
#    print('Você reprovou, se esforce mais')
# else:
#    print('Parabéns, você foi aprovado')
