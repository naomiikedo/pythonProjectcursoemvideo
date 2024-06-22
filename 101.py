from datetime import datetime
def voto(ano):
    idade= datetime.now().year-aniversario
    if idade <16:
        print (f'com {idade} anos  nao pode votar')
    elif idade <=16 or idade<18 or idade>65:
        print (f'com {idade} anos o voto e opcional')
    else:
        print (f'com {idade} anos o voto e obrigatorio')
aniversario=int(input('ano de nascimento:'))
voto(aniversario)