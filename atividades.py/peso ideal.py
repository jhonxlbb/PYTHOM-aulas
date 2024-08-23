import os
os.system("cls || clear")

resultado = 0

print("""
Descrubra o seu peso ideal!!!
      
M - masculino
F - feminino
      """)

sexo = input("Primeiro digite qual o seu sexo: ").upper()
altura = float(input("Agora digite sua altura: "))

match(sexo):
    case "M":
        resultado = (72.7 * altura) - 58
    case "F":
        resultado = (62.1 * altura) - 44.7

print(f"O peso ideal seria: {resultado: .2f}Kg")