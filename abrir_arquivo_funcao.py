#!/usr/bin//python3

def ler_arquivo(nome):
    with open (nome,'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def escrever_arquivo (nome):
    with open (nome,'a') as arquivo:
        conteudo = input('digite uma fruta:')
        arquivo.write(conteudo +'\n')
    return True

def sobrescrever_arquivo(nome):
    with open (nome, 'w') as arquivo:
        conteudo = input ('digite uma fruta: ')
        arquivo.white(conteudo +'\n')
    return True  


escrever_arquivo('frutas.txt')
print(ler_arquivo('frutas.txt'))