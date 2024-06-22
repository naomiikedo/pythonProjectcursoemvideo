from random import choice
n1=(input('qual o primeiro nome:'))
n2=(input('o segundo nome:'))
n3=(input('o terceiro nome:'))
n4=(input('o quarto nome:'))
nomes=[n1,n2,n3,n4]
sorteado=choice(nomes)
print('o nome sorteado foi {}'.format(sorteado))