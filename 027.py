nome=str(input('qual o seu nome completo?')).strip()
n=nome.split()
print('o primeiro nome nome e: {}'.format(n[0]))
print('o ultimo nome e: {}'.format(n[len(n)-1]))