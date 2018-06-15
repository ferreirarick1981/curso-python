soma=0
for x in range (4):
    nota = float(input('Digite a nota {}: '.format(x+1)))
    soma +=nota
print ('A média é igual há {:.2f}'.format(soma/4))