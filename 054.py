menor=0
maior=0
from datetime import date
atual=date.today().year
for c in range(1,8):
    ano=int(input('digite o ano de nascimento:'))
    idade=atual-ano
    if idade<21:
        menor=menor+1
    else:
        maior=maior+1
print('{} sao menores de idade e {} sao maiores de idade'.format(menor,maior))