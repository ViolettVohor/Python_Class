try:  # Será tentado executar esse bloco de código
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b

# except Exception as erro:  # Caso ocorra um erro será executado esse bloco
#    print(f'Problema encontrado: {erro.__class__}')

except (ValueError, TypeError):  # Exceção
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:  # Exceção
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

else:  # Caso não ocorra um erro será executado esse bloco
    print(f'O resultado é {r}')

finally:  # No final será esse bloco, mesmo que tenha ocorrido um erro ou não
    print('Volte Sempre!!')
