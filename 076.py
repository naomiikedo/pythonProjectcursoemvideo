listagem=('lapis',1,'caderno',15.90,'estojo',5,'caneta',1.50,'mochila',120.00)
print(f'{"listagem de preços":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos %2==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R$:{listagem[pos]:>7.2f}')
print('-' * 40)