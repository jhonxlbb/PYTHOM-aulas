import os
os.system("cls || clear")


print("""
===OPERAÇÕES===
(+) para soma
(-) para subtração
(*) para multiplicação
(/) para divisão
      """)

numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("digite o segundo valor: "))
operacao = input("escolha a operação: ")

match(operacao):
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "*":
        resultado = numero1 * numero2
    case "/":
        resultado = numero1 / numero2
    case "_":
        print("operação inexistente.")

print(f"RESULTADO É IGUAL A: {resultado}")