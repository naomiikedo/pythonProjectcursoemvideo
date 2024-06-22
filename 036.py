vc=float(input('qual o valor da casa que deseja comprar?'))
salario=float(input('qual o valor do seu salario?'))
anos=int(input('em quantos anos deseja pagar?'))
mensalidade=vc/(anos*12)
minimo=salario*30/100
if mensalidade > minimo:
    print('EMPRESTIMO NEGADO')
else:

    print('EMPRESTIMO APROVADO')
    print('voce pagara {:.2f} por mes de prestacao'.format(mensalidade))