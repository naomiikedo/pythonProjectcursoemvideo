import math
a=int(input('digite o angulo:'))
seno=math.sin(math.radians(a))
tang=math.tan(math.radians(a))
coss=math.cos(math.radians(a))
print('com um angulo de {:.2f}'.format(a))
print('a tangente sera {:.2f}'.format(tang))
print('o cosseno vale {:.2f}'.format(coss))
print('o seno sera {:.2f}'.format(seno))