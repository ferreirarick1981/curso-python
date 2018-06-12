#!/usr/bin//python3

#Faça uma lista de 10 números, faça um for na lista e imprima somente os numeros pares

nomes = ['André','Pedro','Ricardo','Amauri','Joaquim','Daniel',
'Abel','Clara','Joana']
nomes [0]= 'Barbara'

nomes.append('Eduardo')

nomes.insert(0, 'patrão')
for nome in nomes:
    print('Seja Bem Vindo {}'.format(nome.title()))

while len (nomes) > 0:
    print(nomes)
    nomes.pop()
print(nomes)

name= 'daniel'
name[::-1]
