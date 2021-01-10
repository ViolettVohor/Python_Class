num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O\033[37;1m PRIMEIRO\033[m valor é\033[36;1m maior')
elif num2 > num1:
    print('O\033[37;1m SEGUNDO\033[m valor é\033[36;1m maior')
else:
    print('Os dois valores são\033[36;1m iguais')
