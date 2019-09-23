#!/usr/bin/python3

class Funcionario:
    def __init__(self):
        self.id = 1
        self.nome = "Regis Bracini"
        self.salario = float(25000)

    def consulta_funcionario(self):
        print("O funcionario cadastrado é: {}, com o salário atual de: {}".format(self.nome, self.salario))

    def aumenta_salario(self, salario):
        self.salario = salario

empregado = Funcionario()
empregado.consulta_funcionario()
empregado.aumenta_salario(30000)
empregado.consulta_funcionario()