#!/usr/bin/python3

#Media de duas notas
""" 
print(8*"###")
print("Calculo de nota média!!!")
print(8*"###")
print("\n")
notaA = float(input("Digita a primeira nota: "))
notaB = float(input("Digita a segunda nota: "))

media = notaA + notaB/2
print("\nA nota média é: ", media) 
"""

#Media de notas de acordo com a qtd que o usuário digita
print(8*"###")
print("Calculo de nota média!!!")
print(8*"###")
print("\n")
qtd = int(input("Digita a quantidade de notas a serem calculadas: "))
soma = 0
reduzir = 0

if qtd < 2:
    print("\nQuantidade informada insuficiente. Fim do programa!\n")
else:
    for x in range(qtd):
        nota = float(input("Digita a nota {}: ".format(x+1)))
        if nota > 10:
            print("\nNota {} não computada\n".format(nota))
            reduzir += 1
            continue        
        soma += nota

    media = soma/(qtd-reduzir)
    print("\nA nota média é: {}".format(media))