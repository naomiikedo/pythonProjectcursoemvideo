resposta='s'
c=0
soma=0
maior=0
menor=0
while resposta =='s':
    n=int(input('digite um numero:'))
    soma+=n
    c+=1
    if c==1:
        menor=n
        maior=n
    else:
        if n < menor:
            menor=n
        else:

            maior=n
        resposta = str(input('deseja continuar?'))
print('a media de todos os valores e {}'.format(soma/c))
print('o maior numero digitado foi {} e o menor {}'.format(maior,menor))