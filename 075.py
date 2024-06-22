n1=int(input('figite o 1 valor:'))
n2=int(input('digite o segundo valor:'))
n3=int(input('digite outro valor:'))
n4=int(input('digite o ultimo valor:'))
p=n1,n2,n3,n4
print(f'o numero 9 apareceu {p.count(9)} vezes')
if 3 in p:
    print(f'a posicao que o numero 3 foi digitado foi:{p.index(3)+1}')
else:
    print('o numero 3 nao foi digitado em nenhuma posicao')
for n in p:
    if n%2==0:
        print(f'e par o numero:{n}')