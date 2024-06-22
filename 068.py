from random import randint
v=0
while True:
    jogador=int(input('diga um valor:'))
    computador=randint(1,10)
    tot-jogador+computador
    tipo=''
    while tipo not in 'PI':
        tipo=str(input('par ou impar?')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador jogou {computador} o total e {tot}')

    if tipo == 'P':
            if tot%2==0:
                print('voce venceu')
            v+=1
            else:
                print('voce perdeu')
                break
    elif tipo=='I':
            if tot%2==1:
             print('voce venceu')
              v+=1
            else:
                print('voce perdeu')
                break
    print('vamos jogar novamente')
print(f'game over!voce venceu {v} vezes')