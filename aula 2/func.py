#!/usr/bin/python3

#Transforma args em uma tupla
def teste1(nome, sobrenome, *args):
    print(nome,sobrenome,args)

teste1('Regis','Bracini', 1,2,3,4,5)

#Transforma em uma tupla
def teste2(**kwargs):
    print(kwargs)

teste2(nome='Regis',sobrenome='Bracini')