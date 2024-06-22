from random import randint
computador=randint(0,10)
print('sou o seu computador e acabei de pensar um numero,sera que voce consegue adinhar?')
jogador=0
tentativas=0
while computador!=jogador:
    jogador=(int(input('tente adicinhar qual numero o computadpr escolheu:')))
    tentativas+=1
    if computador > jogador:
        print('mais...tente novamente')
    elif computador<jogador:
        print('menos...tente novamente')
print('computador escolheu:{}'.format(computador))
print('voce acertou')
print('voce precisou de {} tentativas'.format(tentativas))

