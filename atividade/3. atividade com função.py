import os
os.system ("cls || clear")

#Crie um algoritmo que preencha um vetor com 5 números, mostre a quantidade de números negativos e a soma dos números positivos desse vetor.

quantidade_numero = 5 

def solicitar_dados():
    lista_numeros = []
    for i in range(quantidade_numero):
        numero = int(input(f"Digite p { i + 1}º número: "))
        lista_numeros.append(numero)
    return lista_numeros

def verificar_positivos_negativos(lista):
    quantidade_negativo = 0
    soma_positivo = 0
    for numero in lista:
        if numero < 0:
            quantidade_negativo += 1
        else:
            soma_positivo += numero
    return quantidade_negativo, soma_positivo

lista = solicitar_dados()
quantidade_negativo, soma_positivo = verificar_positivos_negativos(lista)

print(f"\nQuantidade de números negativos: {quantidade_negativo}")
print(f"Soma de números positivos: {soma_positivo}")







