# limpa o terminal
import os 
os.system("cls || clear")
import random 

"""
# Crie um algoritimo que leia 5 números inteiros e, em seguida
mostre na tela:
1. A quantidade de números pares e ímpares;
2. A quantidade de números positivos e negativos;
3. A quantidade de números inseridos;
4. O maior e o menor número;
5. A média de números pares;
6. A média de números ímpares;
7. A média de todos os números inseridos;
8. Mostrar os números lidos na ordem inversa.
"""

# Equipe: Leonardo Aráujo, João Felipe, Itauã 

#declarando valores
QUANTIDADE_NUMEROS = 5
lista_numeros = []
contador = 0
maximo_numero = 0
minimo_numero = 0


    
def verificar_pares_impares(lista_numero):
    contador_par = 0
    contador_impar = 0
    for numero in lista_numero:
        if numero % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1
    return contador_par, contador_impar 



for i in range (5):
    numero = random.randint(-10,10)
    lista_numeros.append(numero)
    contador += 1


par, impar = verificar_pares_impares(lista_numeros)


def verificar_positivos_negativos(lista_numero):
    contador_positivo = 0
    contador_negativo = 0
    for numero in lista_numero:
        if numero > 0:
            contador_positivo += 1
        else:
            contador_negativo += 1
    return contador_positivo, contador_negativo
positivo, negativo = verificar_positivos_negativos(lista_numeros)


def media_pares(lista_numero):
    soma_pares = 0
    quantidade_par = 0
    for numero in lista_numero:
        if numero % 2 == 0:
            soma_pares += numero
            quantidade_par += 1
    if quantidade_par > 0:
        return soma_pares / quantidade_par
    return 0


def media_impares(lista_numero):
    soma_impares = 0
    quantidade_impar = 0
    for numero in lista_numero:
        if numero % 2 != 0:
            soma_impares += numero
            quantidade_impar += 1
    if quantidade_impar > 0:
        return soma_impares / quantidade_impar
    return 0


def media_total(lista_numero):
    soma_total = 0
    quantidade_total = 0
    for numero in lista_numero:
        soma_total += numero
        quantidade_total += 1
    if quantidade_total > 0:
        return soma_total / quantidade_total
    return 0
    
       


maximo_numero = max(lista_numeros)
minimo_numero = min(lista_numeros)

print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números impares: {impar}")
print(f"Quantidade de números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")
print(f"Maior número: {maximo_numero}")
print(f"Menor número: {minimo_numero}")
print(f"Quantidade de números inseridos: {contador}")
print(f"A média dos números pares é: {media_pares(lista_numeros)}")
print(f"A média dos números impares é: {media_impares(lista_numeros)}")
print(f"A média de todos os números é: {media_total(lista_numeros)}")
for numero in lista_numeros:
    print(numero)


