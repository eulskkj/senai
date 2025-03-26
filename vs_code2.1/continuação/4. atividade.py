import os
os.system ("cls || clear")

#Construa um algoritmo que calcule a média aritmética de vários valores inteiros positivos, inseridos pelo usuário. 
#O final da leitura acontecerá quando for lido um valor negativo.
#Mostre a média aritmética dos números informados pelo usuário.


soma = 0
contador = 0
while True:
    nota = int(input("Digite sua nota: "))
    if nota <0:
        break
    else:
        soma += nota
        contador += 1
media = soma / contador

print(f"Média: {media}")













