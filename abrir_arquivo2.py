with open ('frutas.txt','r') as arquivo:
    conteudo = arquivo.readlines()
    novo_conteudo = []
    for x in conteudo:
        novo_conteudo.append(x.replace('\n','\t'))
    

with open ('frutas3.txt', 'a') as arquivo:
    for x in novo_conteudo:
        arquivo.write (x)
      

#print (novo_conteudo)