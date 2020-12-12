cid = input('Em que cidade você mora? ')  # .strip()
ci = cid.split()
print(f'Essa cidade tem Santo no começo do nome? \033[1;37m{"SANTO" in ci[0].upper()}\033[m')
print(f'Essa cidade tem Santo no começo do nome? \033[0;36m{"SANTO" == cid[:5].upper()}\033[m')
