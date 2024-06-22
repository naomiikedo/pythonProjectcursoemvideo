n1=int(input('digite o primeiro valor:'))
n2=int(input('digite outro valor:'))
if n1>n2:
    print('{} e o maior numero'.format(n1))
elif n2>n1:
    print('{} e o maior numero'.format(n2))
else:
    print('nao existe numero maior,os dois numeros sao iguais')