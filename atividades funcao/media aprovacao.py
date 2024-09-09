import os 
os.system("cls || clear")


def mediana(n1,n2):
    mediana = (n1 + n2) / 2
    return mediana
def situacao(media):
    if media >= 7:
        return "aprovado"        
    else:
        return "reprovado"


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = mediana(nota1,nota2)
status = situacao(media)

print(f"sua média é: {media}")
print(f"você esta : {status}")
