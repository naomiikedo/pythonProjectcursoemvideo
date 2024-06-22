galera=list()
pessoa=dict()
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('nome:'))
    while True:
        pessoa['sexo']=str(input('sexo[m/f]:')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('erro.digite somente M ou F.')
    pessoa['idade']=int(input('idade:'))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp=str(input('deseja continuar?[s/n]:')).upper()[0]
        if resp in 'SN':
            break
        print('erro.digite somente S ou N.')
    if resp == 'N':
        break
print(galera)
print(f'foram cadrastadas {len(galera)} pessoas')
media=soma/len(galera)
print(f'a media de idade ta galera e {media}')
print('as mulheres cadrastadas foram:',end='')
for p in galera:
    if p['sexo']=='F':
        print(f'{p["nome"]}',end=',')
print()
print(f'pessoas com idade acima da media:',end='')
for p in galera:
    if p['idade']> media:
        print(f'{p["nome"]}',end=',')
print()
