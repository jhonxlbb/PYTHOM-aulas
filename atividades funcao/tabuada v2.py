import os 
os.system("cls || clear")

def tabuada(n1,n2):
    calculo = n1 * n2
    return calculo, resultado

numero1 = int(input("Digite o numero que deseja saber a tabuada: "))

for i in range(1,11):
    resultado = print(f"{numero1} x {i} = {numero1 * i}")
    (resultado)