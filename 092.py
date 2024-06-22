from datetime import datetime
dados={}
dados['nome']=str(input('nome:'))
nasc=int(input('ano de nascimento'))
dados['idade']=datetime.now().year-nasc
dados['carteira de trabalho']=int(input('carteira de trabalho:(0 se noa tiver)'))
if dados['carteira de trabalho']!=0:
    dados['contratacao']=int(input('ano de contratacao:'))
    dados['salario']=float(input('salario:'))
    dados['aposentadoria']=dados['idade']+((dados['contratacao']+35) - datetime.now().year)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')
