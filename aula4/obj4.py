#!/usr/bin/python3

class Calculadora:

    def somar(self, num1, num2):
        return num1 + num2

    def subtrair(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        return num1 / num2


calc = Calculadora()
print(calc.somar(10,2))
print(calc.multiplicar(10,2))
print(calc.subtrair(10,2))
print(calc.dividir(10,2))