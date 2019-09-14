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

#Funcoes
def calcular_media(notas):

    soma = 0
    total = len(notas)

    for x in range(total):
        soma += x

    media = soma/(total)
    return media

def obter_notas():
    print("Digite as notas a serem calculadas, separado por ','")
    notas = input("Notas: ")
    return list(int(x) for x in notas.split(","))


#Media de notas de acordo com a qtd que o usuário digita
print(8*"###")
print("Calculo de nota média!!!")
print(8*"###")
print("\n")

try:
    notas = obter_notas()
    print("\nA nota média é: {}".format(calcular_media(notas)))
    
except Exception as e:
    print("Falha!! {}".format(e))