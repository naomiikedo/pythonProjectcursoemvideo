n=int(input('digite um numero qualquer:'))
bc=int(input('''escolha qual sera a base de conversao:
 [1] para binario
 [2] para octal
[3] para hexadecimal
opçao:'''))

if bc==1:
    print('O numero {} em binario e {}'.format(n,bin(n)[2:]))
elif bc==2:
    print('o numero {} escrito em octal e {}'.format(n,oct(n)[2:]))
elif bc==3:
    print('o numero {} escrito em hexadecimal e {}'.format(n,hex(n)[2:]))
else:
    print('opçao invalida')