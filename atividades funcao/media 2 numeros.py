import os 
os.system("cls || clear")

def media_aritimetica(n1, n2):
    media = (n1 + n2) / 2
    return media

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

media = media_aritimetica(numero1, numero2)

print(f"a média das notas resultam em: {media}")