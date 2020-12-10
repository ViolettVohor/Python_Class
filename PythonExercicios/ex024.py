cid = input('Em que cidade você mora? ')  # .strip()
ci = cid.split()
print(f'Essa cidade tem Santo no começo do nome? {"SANTO" in ci[0].upper()}')
print(f'Essa cidade tem Santo no começo do nome? {"SANTO" == cid[:5].upper()}')
