tot=0
n=int(input('digite um numero:'))
for c in range(1,n+1):
    if n%c==0:
        print( '\033[34m',end='')
        tot+=1
    else:
        print('\033[m',end='')
    print(c,end='')
print('\n\033[mo {} foi divido {}x'.format(n,tot))
if tot==2:
    print('por isso o numero e primo')
else:
    print('por isso o numero nao e primo')