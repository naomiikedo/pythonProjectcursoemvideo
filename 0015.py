dias=int(input('quantos dias ficou com o carro?'))
km=float(input('quantos km foram rodados?'))
pago=(dias*60)+(km*0.15)
print('TOTAL={:.2f}'.format(pago))