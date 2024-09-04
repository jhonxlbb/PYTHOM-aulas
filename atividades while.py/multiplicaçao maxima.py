import os 
os.system("cls || clear")

contador = 0

numero = int(input("Digite o numero inicial: "))
fator = int(input("digite o fator para multiplicar: "))

while True:
    if numero < 100:
        numero = numero * fator
        contador = contador + 1
    else:
        break
print(f"produto final: {numero}")
print(f"contador: {contador}")