peso=float(input('qual o seu peso:'))
altura=float(input('qual a sua altura:'))
imc=peso/(altura**2)
print('seu imc e {}'.format(imc))
if imc <18.5:
    print('voce esta abaixo do peso')
elif imc <=25:
    print('peso ideal')
elif imc <=30:
    print('sobrepeso')
elif imc <=40:
    print('obesidade')
else:
    print('obsidade morbida')