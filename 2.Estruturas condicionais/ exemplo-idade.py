import os
os.system("cls || clear")

#solicitando dados
idade = int(input("Digite sua idade: "))

#verificando
if idade < 18:
    print("Menoridade")
    print("===FIM===")
else:
    print("maioridade")
    print("===FIM===")
    