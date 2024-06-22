def ajuda(com):
    help(com)
def titulo(msg,cor=0):
    tam=len(msg)
    print('-='*tam)
    print(msg)
    print('-='*tam)

comando=''
while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando=str(input('funcao ou biblioteca>'))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('ate logo')