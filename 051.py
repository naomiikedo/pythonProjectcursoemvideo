p=int(input('primeiro termo:'))
r=int(input('razao:'))
d= p+(10-1)*r
for c in range(p,r,d):
    print('{}'.format(c))