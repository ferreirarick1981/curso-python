#As instrucoes da funcao 

def alteracao(nome, origin, destino):
    with open (nome,'r') as arquivo:
        conteudo = arquivo.readlines()
        novo_conteudo = []
        for x in conteudo:
            novo_conteudo.append(x.replace(origin,destino))
    return novo_conteudo

#Monta-se a variavel para a funcao 
conteudo = alteracao('frutas.txt', 'e', '&')
with open ('frutas2a.txt','a')as arquivo:
    for x in conteudo:
        arquivo.write(x)