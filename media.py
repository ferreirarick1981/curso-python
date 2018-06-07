#!/usr/bin//python3

#Leia um nome de um aluno, e leia duas notas, calcule e média do aluno 

aluno = input('Digite o nome do aluno')
n1= int(input('Digite a primeira nota'))
n2= int(input('Digite a segunda nota'))
falta = int(input('Digite a quantidade de faltas'))
media =(n1+n2)/2
if media >=7 and falta <=4:
    resultado = 'aprovado'
else:
    resultado = 'reprovado'
print('O aluno{} teve a média de {} e foi {}'.format(aluno.title(),media, resultado))