sal=float(input('qual o valor do seu salario?'))
if sal>1250.00:
    nsal=sal+(sal*10)/100
else:
    nsal=sal+(sal*15)/100
    print('seu novo salario e de {}'.format(nsal))