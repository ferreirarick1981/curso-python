#!/usr/bin//python3

#manipula o arquivo

with open('frutas.txt', 'r') as f:
    conteudo = f.readlines()
    aux = []
    for x in conteudo:
        x= x.replace ('\n','')
        aux.append(x)
print(aux)
aux.append('pêssego')
aux.insert(0,'Kiwi')
with open ('frutas2.txt','w')as arquivo:
    for item in aux:
        arquivo.write ('{}\n'.format(item.title()))
       
