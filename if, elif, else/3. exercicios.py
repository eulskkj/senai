import os
os.system("clear")

#Elabore um algoritmo para solicitar ao usuário um valor e escrever a
#mensagem: “É MAIOR QUE 10!”. 
#Se o valor lido for maior que 10, caso contrário escrever “NÃO É
#MAIOR QUE 10!”
#Verifique se o número digitado é igual a 10, caso seja, escreva a
#mensagem: “O número é igual a 10!”

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
terceira_nota = float(input("Digite sua terceira nota: "))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3

print (f"Média: {media}")

if media < 7:
    print ("Reprovado!")
else:
    print ("Aprovado!")