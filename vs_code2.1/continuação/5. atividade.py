import os
os.system ("cls || clear")

#Faça um algoritmo que leia uma quantidade não
#determinada de números inteiros positivos. Calcule: 
#quantidade de números pares e ímpares; 
#média de valores pares 
#média geral dos números lidos. 
#O número que encerrará a leitura será o número zero.

#media global
soma = 0
contador = 0
#media pares
quantidade_pares = 0
soma_pares = 0
#quantidade impar
quantidade_impares = 0 
while True:
    numero = int(input("Digite um número: "))

    #parar no 0
    if numero == 0:
        break
    soma += numero
    contador += 1
    #pares
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    #impares    
    else:
        quantidade_impares += 1

    contador += 1
    soma += numero
    
if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0
media = soma / contador




   
print(F"Media: {media}")
print(f"Media pares: {media_pares}")
print(f"Quantidade impares: {quantidade_impares}")
print(f"Quantidade pares: {quantidade_pares}")










