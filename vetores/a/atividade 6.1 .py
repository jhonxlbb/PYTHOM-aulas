import os 
os.system("cls || clear")


lista_numeros = []
def tranformar(n1):
    if n1 < 0:
        n1 = 0
        return tranformar
# solicitando dados
for i in range(5):
    numero = int(input("Digite um número: "))
    numero = tranformar(numero)
    lista_numeros.append(numero)

#exibindo resultados 

print(f"{i+1}º número: {numero}")
