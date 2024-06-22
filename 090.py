dados={}
dados['nome']=str(input('digite seu nome:'))
dados['media']=float(input('qual a media do aluno:'))
if dados['media'] <5:
    print(dados)
    print('aluno retido')
else:
    print(f'o aluno {dados["nome"]} ')
    print(f'a media foi {dados["media"]}')

    print('aluno aprovado')