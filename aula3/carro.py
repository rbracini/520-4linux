#!/usr/bin/python3

class Veiculo:
    nome = ""
    tipo = "car"
    cor = ""
    valor = 100.00
    def descricao(self):
        desc_str = "%s é %s %s e custa $%.2f." % (self.nome, self.tipo, self.cor, self.valor)
        return desc_str

car1 = Veiculo()
car1.nome = "Ferrari"
car1.cor = "Vermelha"
car1.tipo = "Conversível"
car1.valor = 600000.00

car2 = Veiculo()
car2.nome = "Perua"
car2.cor = "Azul"
car2.tipo = "Van"
car2.valor = 10000.00

# test code
print(car1.descricao())
print(car2.descricao())