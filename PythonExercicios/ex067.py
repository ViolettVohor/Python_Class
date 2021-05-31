while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if n < 0:
        break
    for i in range(0, 11, 1):
        print(f'{n} X {i} = {n*i}')
    print('-' * 20)
