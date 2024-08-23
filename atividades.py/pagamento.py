import os
os.system("cls || clear")

#declarando variaveis
desconto : float
pagamento_final : float
preco_parcelado : float
#solicitando dados 
valor_produto = int(input("Digite o valor do produto: "))
print("""
1- pagamento à vista
2- Pagamento à prazo
""")
pagamento = int(input("Digite a Forma de pagamento : "))
#calculos
desconto = valor_produto * 0.10

if pagamento == 1:
    pagamento_final = valor_produto - desconto
    print(f"Valor do produto: R${valor_produto: .2f}")
    print(f"Forma de Pagamento: à vista")
    print(f"Valor do desconto: R${desconto: .2f}")
    print(f"TOtal a pagar: R${pagamento_final: .2f}")


if pagamento == 2:
    print("""
máximo de até 6 parcelas!!!
          """)
    parcelas = int(input("digite a quantidade de parcelas: "))
if parcelas == 2:
    preco_parcelado = valor_produto / 2
    print(f"Valor do produto: R${valor_produto}")
    print("Forma de pagamento: à prazo.")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor por parcelas: R${preco_parcelado}")
    print(f"Valor Total: R${valor_produto}")

if parcelas == 3:
    preco_parcelado = valor_produto / 3
    print(f"Valor do produto: R${valor_produto}")
    print("Forma de pagamento: à prazo.")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor por parcelas: R${preco_parcelado}")
    print(f"Valor Total: R${valor_produto}")

if parcelas == 4:
    preco_parcelado = valor_produto / 4
    print(f"Valor do produto: R${valor_produto}")
    print("Forma de pagamento: à prazo.")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor por parcelas: R${preco_parcelado}")
    print(f"Valor Total: R${valor_produto}")

if parcelas == 5:
    preco_parcelado = valor_produto / 5
    print(f"Valor do produto: R${valor_produto}")
    print("Forma de pagamento: à prazo.")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor por parcelas: R${preco_parcelado}")
    print(f"Valor Total: R${valor_produto}")

if parcelas == 6:
    preco_parcelado = valor_produto / 6
    print(f"Valor do produto: R${valor_produto}")
    print("Forma de pagamento: à prazo.")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor por parcelas: R${preco_parcelado}")
    print(f"Valor Total: R${valor_produto}")
