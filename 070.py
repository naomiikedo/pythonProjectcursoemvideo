continuar='s'
tot=0
mais=0
menornome=''
menor=0
c=0
while True:
    nome=str(input('digite o nome do produto:'))
    preco=float(input('digite o preço:'))
    continuar=' '
    tot+=preco
    c+=1
    if c==1:
        menor=preco
    while continuar not in 'sn':
        continuar=str(input('deseja continuar?[s/n]'))

    if continuar=='n':
         break
    if preco>1000:
        mais+=1
    if preco < menor:
        menor=preco
        menornome=nome
print(f'o total  a se pagar e {tot},{mais} custaram mais de 1000 reais,e o produto mais barato e {menornome}')