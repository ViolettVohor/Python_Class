ent = input('Digite algo: ')
color = {'m': '\033[34;1m', 'l': '\033[m', 'v': '\033[32;1m'}
# Cria um dicionário chamado color com as chaves 'm' de magenta, 'l' de limpar e 'v'  de verde
print(type(ent))
# mostra o tipo da variável
print(f'Está tudo em minúsculo? {color["m"]}{ent.islower()}{color["l"]}')
# mostra se o valor da variável são minúsculas
print(f'Está tudo em maiúsculo? {color["v"]}{ent.isupper()}{color["l"]}')
# mostra se o valor da variável são maiúsculas
print(f'É alfanúmerico? {color["m"]}{ent.isalnum()}{color["l"]}')
# Verifica se o valor da variável é alfanúmerico
print(f'É alfabético? {color["v"]}{ent.isalpha()}{color["l"]}')
# Verifica se o valor tem apenas letras
print(f'É númerico? {color["m"]}{ent.isnumeric()}{color["l"]}')
# Verifica se o valor tem apenas números
print(f'É ASCII? {color["v"]}{ent.isascii()}{color["l"]}')
# Verifica se o valor tem ASCII (símbolos)
print(f'É decimal? {color["m"]}{ent.isdecimal()}{color["l"]}')
# Verifica se o valor é decimal
print(f'É um digito? {color["v"]}{ent.isdigit()}{color["l"]}')
# Verifica se o valor é um digito
print(f'É um identificador? {color["m"]}{ent.isidentifier()}{color["l"]}')
# Verifica se o valor serviria como identificador
print(f'É possível mostrar todos os caracteres? {color["v"]}{ent.isprintable()}{color["l"]}')
# Verifica se todos caracteres são possíveis de mostrar
print(f'Todas as palavras estão capitalizadas? {color["m"]}{ent.istitle()}{color["l"]}')
# Verifica se todos as palavras estão com a primeira letra maiúsculas
print(f'Todos os caracteres são espaços? {color["v"]}{ent.isspace()}{color["m"]}')
# Verifica se a variável tem apenas espaços
