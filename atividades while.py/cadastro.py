import os
os.system("cls || clear")

contador = 0
soma = 0

while True:
    nota = float(input("Digite uma nota: "))
    if nota > 0:
        contador += 1
        soma += nota

    else:
        nota < 0
        break
media = soma / contador
print(f"Média: {media}")