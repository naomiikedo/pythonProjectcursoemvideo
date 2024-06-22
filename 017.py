import math
co=float(input('qual o comprimento do cateto oposto?'))
ca=float(input('qual o comprimento do cateto adjacente?'))
hi=math.hypot(co,ca)
print('a hipo2tenusa vai valer {:.2f}'.format(hi))