km=int(input('quantos km de distancia?'))
if km<=200:
    p1=km*0.50
    print('voce pagara {}'.format(p1))
else:
    p1=km*0.45
    print('voce pagara {}'.format(p1))