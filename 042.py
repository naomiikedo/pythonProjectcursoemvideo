n1=int(input('primeiro segmento:'))
n2=int(input('segundo segmento:'))
n3=int(input('terceiro segmento:'))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('os segmentos podem formar um triangulo')
    if n1==n2==n3:
        print('triangulo equilatero')
    elif n1==n2 or n1==n3 or n2==n3:
        print('triangulo isosceles')
    else:
        print('triangulo escaleno')
else:
    print('nao pode formar um triangulo')