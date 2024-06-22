idademaior=0

m20=0
hmv=''
idadem=0
for c in range(1,5):
    nome=input('digite o nome:')
    idade=int(input('digite a idade:'))
    sexo=input('digite o sexo: F/M:')
    idadem=idadem+idade

    if sexo=='f' and idade<=20:
        m20=m20+1
    if sexo=='m' and idade>idademaior:
        hmv=nome
        idademaior=idade
media=idadem/4
print('o nome do homem mais velho e {} e ele tem {} anos,mulheres com menos de 20 anos {},a media de idades digitadas  foi {}'.format(hmv,idademaior,m20,media))