from random import choice
n=[0,1,2,3,4,5]
sorteado=choice(n)
na=int(input('qual numero voce acha que foi sorteado?'))
print(sorteado)
if sorteado== na:
    print('foi sorteado o numero {},voce acertou!'.format(sorteado))
else:
    print('foi sorteado o numero {},voce perdeu!'.format(sorteado))