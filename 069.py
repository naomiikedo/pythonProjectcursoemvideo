continuar='s'
menos20=0
maior18=0
totm=0
while True:
    idade=int(input('idade:'))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('sexo:')).strip().upper()[0]
    if idade > 18:
        maior18+=1
    if sexo=='m':
        totm+=1
    if sexo=='F' and idade <20:
        menos20+=1
    while continuar not in 'SN':
        continuar=str(input('deseja continuar?[s/n]')).strip().upper()[0]
    if continuar =='N':
        break
print(f'foram cadastrados {maior18} maisores de 18 anos,{totm} total de homens,e mulheres abaixo dos 20 anos {menos20} ')
