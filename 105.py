def notas(*n,situacao=False):
    r=dict()
    r['total']= len(n)
    r['maior']= max(n)
    r['menor']=min(n)
    r['media']=sum(n)/len(n)

    if situacao:
        if r['media']>=7:
            r['situacao']='boa'
        elif r['media']>=5:
            r['situacao']='razoavel'
        else:
            r['situacao']='ruim'
    return r


resp=notas(6.0,7,5.5,situacao=True)
print(resp)