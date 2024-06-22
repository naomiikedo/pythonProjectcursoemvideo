palavras=('onibus','janela','fogao','esteira','feijao','programacao')
for p in palavras:
    print(f'\nna palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end='')