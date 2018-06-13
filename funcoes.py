#!/usr/bin//python3

def boas_vindas(nome):
    nome = nome.replace('a', '@')
    return 'Seja bem vindo, {}'.format (nome. title())
nomes = ['daniel','4linux', 'alessandra']

for nome in nomes:
    print(boas_vindas(nome))