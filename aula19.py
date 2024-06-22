dados={'nome':'Pedro','idade':'25'}
print(f'o nome e {dados["nome"]}, e ele tem {dados["idade"]} anos ')
dados['sexo']='M'
print(dados['sexo'])
for k,v in dados.items():
    print(f'o {k} e {v}')