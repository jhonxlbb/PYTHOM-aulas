import os
os.system("cls || clear")

def tabuada (n1,n2):
    calculo = n1 * n2
    return calculo

numero1 = int(input("Digite um numero para saber sua tabuada: "))

for i in range(1,11):
    resultado = tabuada(numero1, i)
    print(f"{numero1} x {i} = {resultado} ")