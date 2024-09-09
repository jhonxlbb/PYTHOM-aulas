import os
os.system("cls || clear")

for i in range(3):
    nota = float(input(f"digite a {i+1}º nota: "))

def media_aritimetica(n1):
    media = nota / 3
    return media
media = media_aritimetica(nota)

print(f"média é igual a:{media}")