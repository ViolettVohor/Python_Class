def escreva(msg):  # Escreva a frase com uma borda personalizado pelo tamanho da frase
    tam = len(msg) + 4
    print('~'*(tam))
    print(f'  {msg}')
    print('~'*(tam))


escreva('Matheus Farias')  # Chama a função 'escreva' que escreve a frase de uma forma personalizada
escreva('Curso de Python no Youtube')
escreva('CEV')
