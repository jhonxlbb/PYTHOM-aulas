import os
os.system("cls || clear")

contador = 0
numero = 0

while True:
    numero = int(input("Digite um número negativo: "))
    if numero < 0:
        contador = contador + 1
    else:
        print(f"você selecionou {contador} números negativos")
        break