import os
os.system("cls || clear")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite o sua altura: "))

def indice_massa_corporea(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificacao(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc >= 18.5 and imc < 24.9:
        return "peso normal"
    elif imc >= 25 and imc <= 29.9:
        return "sobrepeso"
    elif imc >= 30 and imc < 34.9:
        return "obesidade grau 1"
    elif imc >= 35 and imc <= 39.9:
        return "obesidade grau 2"
    else:
        return "obesidade grau 3 ou thais carla"

imc = indice_massa_corporea(peso, altura)
classe = classificacao(imc)
print(f"IMC: {imc:.2f}")
print(f"classificação: {classe}")