n=0
tot=0
soma=0
n=int(input('digite um numeros:[999 para parar]'))
while n !=999:
    tot+=1
    soma+=n
    n = int(input('digite um numeros:[999 para parar]'))
print('foram digitados:{} numeros'.format(tot))
print('o total da soma foi {}'.format(soma))