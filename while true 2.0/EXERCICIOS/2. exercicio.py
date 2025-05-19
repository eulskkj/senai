import os
os.system ("cls || clear")

#Escreva um algoritmo que solicite duas notas para um aluno. 
#Caso seja menor que 0 ou maior que 10, mostre a pergunta
#novamente.
#Calcule e mostre a média aritmética do aluno.

QUANTIDADE_NOTAS = 2
soma = 0

for i in range (QUANTIDADE_NOTAS):
    while True:
        nota = float(input("Digite uma nota: "))

        if nota < 0 or nota > 10:
            print(f"A nota deve ser entre 0 e 10. \n") 
        else:
            soma += nota
            break
media = soma / QUANTIDADE_NOTAS
print(f"Média: {media}")







