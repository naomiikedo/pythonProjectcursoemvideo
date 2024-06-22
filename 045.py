from random import randint
itens=('pedra','papel','tesoura')
computador=randint(0,2)
print('''suas opcoes sao:
[0] pedra
[1] papel
[2] tesoura''')
jogador=int(input('qual voce escolhe?'))
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
if computador==0:
    if jogador==0:
        print('empate')
    elif jogador==1:
        print('jogador ganhou')
    elif jogador==2:
        print('computador ganhou')
    else:
        print('opcao invalida')
if computador==1:
    if jogador==0:
        print('computador ganhou')
    elif jogador==1:
        print('empate')
    elif jogador==2:
        print('jogador ganhou')
    else:
        ('opcao invalida')
if computador==2:
    if jogador==0:
        print('jogador ganhou')
    elif jogador==1:
        print('computador ganhou')
    elif jogador==2:
        print('empate')
    else:
        ('opcao invalida')
