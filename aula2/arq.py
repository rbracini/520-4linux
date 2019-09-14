#!/usr/bin/python3
arquivo = open('./aula2/teste.txt', 'r')

print("print1: ", arquivo.read())

arquivo.close()

# Não precisa se preocupar com o fechamento do arquivo utilizando essa função
with open('./aula2/teste.txt', 'r') as arquivo:
    print(arquivo.read())

with open('./aula2/teste.txt', 'w') as arquivo:
    arquivo.write("Teste de escrita3")

with open('./aula2/letras.txt', 'w') as arquivo:
    letras = [ chr(x)+'\n' for x in range(97, 123)]
    arquivo.writelines(letras)