from Uteis import cores
import urllib.request

try:  # Tenta acessar o site pudim
    site = urllib.request.urlopen('http://pudim.com.br')

except (urllib.error.URLError, ValueError):  # Caso não consiga mostra essa mensagem
    cores(1, 'Não foi possível acessar o Pudim!')

else:  # Se não mostra essa
    cores(3, 'O Pudim foi acessado com sucesso!')
