#!/usr/bin/python3

#Lambda são funções anonimas
lamb = lambda a,b,c:((b**2)-(4*a*c))
print (lamb(3,-2,-5))

#Forma mais comum a ser utilizado
#(lambda argumento1,argumento2 : retorno/calculo)(valorDoArgumento1,valorDoArgumento2)
print((lambda x,y: x+y)(5,7))