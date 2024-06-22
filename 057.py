
sexo=str(input('digite o seu sexo [f/m]:')).strip().upper()[0]
while sexo not in 'mf':
    sexo=str(input('SEXO INVALIDO. diite o seu sexo [f/m]:'))
print('{} sexo registrado'.format(sexo))
