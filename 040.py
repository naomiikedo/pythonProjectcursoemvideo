n1=float(input('primeira nota:'))
n2=float(input('segunda nota:'))
media=(n1+n2)/2
if media <5:
    print('aluno reprovado')
elif media <7:
    print('aluno em recuperaçao')
else:
    print('aluno aprovado')