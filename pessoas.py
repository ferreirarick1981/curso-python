pessoas = [
{'nome':'daniel','idade':24},
{'nome':'guido','idade':59},
{'nome':'diogo','idade':27},
{'nome':'christian','idade':40},
{'nome':'rick','idade':37}
]
#Varias formas de impressão 

#for x in pessoas:
    #print(x['nome'],x['idade'])
    #print(len(pessoas))

#print(type(pessoas))

#for x in pessoas:
    #print (type(x))

#x, t , z são variáveis para pessoa, item, valores 
for x in pessoas:
    for t,z in x.items():
        print(t,z)