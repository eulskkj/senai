import os 
os.system ("cls || clear")

#Crie um programa que leia 6 números, armazenando em um vetor e informe quantos são pares e quantos são ímpares.
#Mostre os números informados pelo usuário.

lista_numeros = []
quantidade_numeros = 6

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero% 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

print("== SOLICITANDO NÚMEROS ==")
for i in range(quantidade_numeros):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1}º número: "))
            lista_numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")
pares, impares = pares_impares(lista_numeros)

print("\n= Resutado =")
print(f"Números digitados: {lista_numeros}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")





