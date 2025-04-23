import os
os.system ("cls || clear")

#Crie um algoritmo que preencha um vetor com 5 números, mostre a quantidade de números negativos e a soma dos números positivos desse vetor.

lista_numeros = []
QUANTIDADE_NUMEROS = 5
quantidade_negativos = 0
quantidade_positivos = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(numero)
for numero in lista_numeros:
    if numero < 0:
        quantidade_negativos += 1
    else:
        quantidade_positivos += numero

print(f"\nQuantidade de números negativos: {quantidade_negativos}")
print(f"\nQuantidade de números positivos: {quantidade_positivos}")




