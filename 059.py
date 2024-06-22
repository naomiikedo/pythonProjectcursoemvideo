n1=int(input('digite um numero:'))
n2=int(input('digite outro numero:'))
escolha=0

while escolha!= 5:
    print('---------MENU--------')
    print('''[1] para somar
    [2] para multiplicar
    [3] para maior
    [4] novos numero
    [5] para sair do programa''')
    escolha=int(input('qual deseja escolher?'))
    if escolha==1:
        print('{}+{}={}'.format(n1,n2,n1+n2))
        print('*******************')
    elif escolha==2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
        print('********************')
    elif escolha==3:
        if n1>n2:
            print('{} e o maior numero'.format(n1))
        else:
            print('{} e o maior numero'.format(n2))
    elif escolha==4:
        n1=int(input('digite um numero:'))
        n2=int(input('digite outro numero:'))
    else:
        print('PROGRAMA FINALIZADO')
