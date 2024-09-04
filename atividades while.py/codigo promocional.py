import os
os.system("cls || clear")

contador = 0 

while True:
    cupom = input("Digite o codigo promocional: ")
    if cupom == "PROMO2024":
        print("codigo aceito")
        break
    else:
        contador += 1
    if contador >= 3:
        print("Codigo invalido")
        break

