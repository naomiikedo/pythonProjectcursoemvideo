from datetime import date
atual=date.today().year
an=int(input('qual o ano do seu nascimento:'))
idade=atual-an
if idade <=9:
    print('mirim')
elif idade <=14:
    print('infantil')
elif idade <=19:
    print('junior')
elif idade <=25:
    print('senior')
else:
    print('master')