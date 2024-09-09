import os 
os.system("cls || clear")

def inflacionar(preco):
    if preco < 100:
        return preco * 1.1
    else:
        return preco * 1.2

preco = float(input("digite o preco do produto: "))

inflacao = inflacionar(preco)

print(f"preco inflacionado é: {inflacao}")

