ano=int(input('qual ano deseja analizar?'))
if ano % 4==0 and ano % 100!=0 or ano %400==0:
    print('o ano {} e bissexto'.format(ano))
else:
    print('o ano {} nao e bissexto'.format(ano))