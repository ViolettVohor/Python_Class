from time import sleep

def maior(*nums):
    maior = 0
    print('-='*30)
    print('Analisando os valores passados...')

    sleep(0.5)
    for num in nums:
        if num > maior:
            maior = num
        print(num, end=' ')
        sleep(0.5)

    print(f'foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
