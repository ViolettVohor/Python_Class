print('oi')
print(x)  # não existe a variável 'x'
# Exceção NameError

n = int(input('Número: '))  # Não aceita tipo string
# Exceção ValueError
print(f'Você digitou o número {n}')

a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a/b  # Não é possível dividir por 0
# Exceção ZeroDivisionError
print(f'O resultado foi {r}')
