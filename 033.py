a=int(input('digite um numero:'))
b=int(input('digite outro numero:'))
c=int(input('digite o terceiro numero:'))
menor=a
if b<a and b<c:
    menor=b
if c<b and c<a:
    menor=c
print('o menor numero e {}'.format(menor))
maior=a
if b>a and b>c:
    maior=b
if c>b and c>a:
    maior=c
print('o maior numero digitado foi {}'.format(maior))


