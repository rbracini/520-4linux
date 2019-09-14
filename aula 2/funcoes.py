#!/usr/bin/python3
produtos = []

def cadastrarProduto(produto):
    global produtos
    produtos.append(produto)

def listarProdutos():
    global produtos
    for p in produtos:
        print(p)

produto = ""
while produto != "sair":
    produto = input("Digite o produto que deseja cadastrar: ")
    cadastrarProduto(produto)
    print("produtos cadastrados")
    listarProdutos()