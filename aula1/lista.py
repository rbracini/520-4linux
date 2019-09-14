#!/usr/bin/python3

alfabet = []

for num_ascii in range(65,91):
    alfabet.append(chr(num_ascii))

print(alfabet)
print(2*"\n")
#O mesmo codigo em 1 linha:
alfabetOnLine = [chr(x) for x in range(97,123)]
print(alfabetOnLine)