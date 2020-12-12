num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro:'))
if num1 > num2:
    print('O primeiro valor é\033[36;1m maior')
elif num2 > num1:
    print('O segundo valor é\033[36;1m maior')
else:
    print('Os dois valores são\033[36;1m iguais')
