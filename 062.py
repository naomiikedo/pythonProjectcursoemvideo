primeiro=int(input('digite o primeiro termo:'))
razao=int(input('digite a razao:'))
termo=primeiro
c=1
total=0
mais=10
while mais!=0:
    total+=mais
    while c<=total:

        print('{}' .format(termo),end='->')
        termo+=razao
        c+=1
    print('pausa')
    mais=int(input('quantos mais deseja fazer?'))
print('progressao finalizada com {} termos mostrados'.format(total))
