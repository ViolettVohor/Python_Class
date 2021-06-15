from time import sleep


def maior(*nums):  # Verifica qual o maior valor dentre os valores passado no parâmetro 'nums'
    major = 0
    print('-='*30)
    print('Analisando os valores passados...')

    sleep(0.5)
    for num in nums:
        if num > major:
            major = num
        print(num, end=' ')
        sleep(0.5)

    print(f'foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {major}')


maior(2, 9, 4, 5, 7, 1)  # Chama que a função 'maior'
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
