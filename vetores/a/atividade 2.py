import os 
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
lista_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)
    
#processamento
soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS

for nota in lista_notas:
    print(f"notas: {nota}")
print(f"Média: {media}")