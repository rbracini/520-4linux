#!/usr/bin/python3

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
soma = 0
cont = 0

for x in matriz:
    #soma += x.index
    for y in x:
        print("Y= ", y)
    print("\nValor: ", x)