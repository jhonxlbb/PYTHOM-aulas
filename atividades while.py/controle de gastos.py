import os 
os.system("cls || clear")

gasto_total = 0
orcamento = float(input("Digite o orçamento:")) 

while True:
    gasto_diario = float(input("Digite o gasto diario: "))
    gasto_total = gasto_total + gasto_diario
    if gasto_total > orcamento:
        print("gasto é maior que o orçamento")
        break
    else:
        print(f"{orcamento - gasto_total}")
        
    