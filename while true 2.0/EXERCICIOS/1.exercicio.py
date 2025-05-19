import os
os.system ("cls || clear")

#Escreva um algoritmo que solicite ao usuário a nota de um
#aluno. 
#Caso seja menor que 0 ou maior que 10, mostre a pergunta
#novamente.
#Mostre a nota informada pelo usuário.



while True:
    nota = float(input("Digite uma nota: "))
    if nota < 0:
        print(f"Nota: {nota}") 
    elif nota > 10:
        print(f"Nota: {nota}")
    else:
        break
        
print(f"Nota: {nota}")






