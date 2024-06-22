preco=float(input('digite o valor da compra R$'))
print('''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista cartao
[3]2x no cartao
[4]3x ou mais no cartao''')
opcao=int(input('qual opçao escolhe:'))
if opcao==1:
    total=preco-(preco*10/100)
    print('voce pagara {:.2f}'.format(total))
elif opcao==2:
        total=preco-(preco*5/100)
        print('voce pagara {:.2f}'.format(total))
elif opcao==3:
    total=preco
    parcela=total/2
    print('voce pagara duas parcelas de {:.2f}'.format(parcela))
elif opcao==4:
    total=preco+(preco*20/100)
    totp=int(input('em quantas parcelas deseja fazer?'))
    parcela=total/totp
    print('sua compra sera parcelada em {}x e voce pagara{} por mes '.format(totp,parcela))
else:
    total=0
    print('opçao invalida.tente novamente')
