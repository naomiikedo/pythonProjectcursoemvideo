from datetime import date
atual=date.today().year
an=int(input('qual o ano do seu nascimento?'))
idade=atual-an
if idade <18:
    print('voce ainda nao esta na epoca de se alistar no serviço militar')
    print('faltam',18-idade,'anos para poder se alistar')
elif idade==18:
    print('ja esta na hora de voce se alistar no serviço militar')
else:
    print('voce ja passou da epoca de se alistar no serviço militar')
    print('voce passou',idade-18,'anos da epoca em que tinha que se alistar' )