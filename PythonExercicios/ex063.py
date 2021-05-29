n1 = 0
n2 = 1
n = int(input('Quantos números da sequência de Fibonacci, você quer ver? '))
c = 0

while c < n:
    c += 1
    if c % 2 != 0:
        print(n1, end=' -> ')
        n1 += n2
    else:
        print(n2, end=' -> ')
        n2 += n1
