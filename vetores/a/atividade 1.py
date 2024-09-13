import os 
os.system("cls || clear")

#entrada.
lista_notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota) #organiza a fila.

#saida

for i, nota in enumerate(lista_notas):
    print(f"Nota: {nota}")
