import urllib.request

try:  # Tenta acessar o site pudim
    site = urllib.request.urlopen('http://pudim.com.br')

except urllib.request.URLError:  # Caso não consiga mostra essa mensagem
    print('\033[31;1mNão foi possível acessar o Pudim!\033[m')

else:  # Se não mostra essa
    print('\033[33;1mO Pudim foi acessado com sucesso!')
