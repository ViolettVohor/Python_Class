seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg3 + seg2 > seg1 and seg3 + seg1 > seg2 and seg2 + seg1 > seg3:
    print('Esses segmentos\033[32;1m podem\033[m formar uma reta.')
    if seg3 == seg2 == seg1:
        print('Esse é um triângulo \033[35;1mEquilátero.')
    elif seg3 != seg2 != seg1 != seg3:
        print('Esse é um triângulo \033[37;1mEscaleno')
    else:
        print('Esse é um triângulo \033[36;1mIsósceles')
else:
    print('Esses segmentos\033[31;1m não podem\033[m formar um triângulo.')
