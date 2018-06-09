#!/usr/bin//python3
with open ('nome.txt','a+')as arquivo:
    while True:
        nome = (input('Digite um nome:'))
        if nome.lower() == 'sair':
            break
        arquivo.write(nome + '\n')