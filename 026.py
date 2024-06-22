frase=str(input('digite uma frase:')).upper().strip()
print('a letra a aparece na frase {}x'.format(frase.count('A')))
print('a primeira letra a aparece na posicao {}'.format(frase.find('A')+1))
print('a ultima vez que A aparece e na posicao {}'.format(frase.rfind('A')+1))

