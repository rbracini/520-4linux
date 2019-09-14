#!/usr/bin/python3

cont = 1
with open('./aula 2/arquivoenum.txt', 'r+') as arquivo:
    linhas = arquivo.readlines()
    arquivo.seek(0)
    for x in linhas:
        #Não coloca contador na linha com espaço
        if not str(x).isspace():
            arq = str(cont) + " - " + x 
            arquivo.write(arq)
            cont += 1
        else:
            arquivo.write(x)