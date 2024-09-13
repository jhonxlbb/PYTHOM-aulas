import os 
os.system("cls || clear")

#entrada.
lista_notas = []

for i in range(2):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota) #organiza a fila.

#saida

for i, nota in lista_notas(enumerate):
    print(f" {i}º Nota: {nota}")
