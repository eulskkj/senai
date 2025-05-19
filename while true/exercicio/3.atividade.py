import os
os.system ("cls || clear")

#Escreva um algoritmo que pergunte ao usuário se deseja inserir
#mais uma nota, 
#se a resposta do usuário for “N”, 
#o programa fará a média aritmética das notas informadas 
#e mostrará a média aritmética para o usuário.
#Obs.: Use um contador dentro do laço de repetição para contar a
#quantidade de iterações (loops).
contador = 0
soma = 0

while True:
    nota = float(input("Digite sua nota: "))
    continuar = input("Deseja inserir mais uma nota? (digite 'S' ou 'N'): ").upper()
    if continuar == "N":
        break 
    else:
        contador += 1
        soma += nota

if contador == 0:
    soma = nota
    contador = 1

media = soma / contador

print(f"\nMédia: {media}")
















