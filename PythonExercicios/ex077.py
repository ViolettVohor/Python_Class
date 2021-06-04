palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'praticar', 'trabalhar',\
    'mercado', 'programador', 'futuro'

for palavra in palavras:  # Percorre os elementos da tupla
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:  # Percorre os caracteres de cada elemento da tupla
        # noinspection SpellCheckingInspection
        if letra.lower() in 'aáàãâeêéiíoôõuú':  # Mostra as vogais
            print(letra, end=' ')
