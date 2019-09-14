#!/usr/bin/python3

#Lambda são funções anonimas
lamb = lambda a,b,c:((b**2)-(4*a*c))
print (lamb(3,-2,-5))

#Forma mais comum a ser utilizado
#(lambda argumento1,argumento2 : retorno/calculo)(valorDoArgumento1,valorDoArgumento2)
print((lambda x,y: x+y)(5,7))

nomes = ['regis','bracini']
result = map(lambda x: x.title(), nomes)
print(list(result))

#Calcula o quadrado perfeito de um range de 10 números
quadrados = map(lambda x: x**2,range(1,11))
print(list(quadrados))