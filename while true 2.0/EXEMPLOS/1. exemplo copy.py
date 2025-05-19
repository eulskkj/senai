import os 
os.system ("cls || clear")



nota = 0
#QUANTIDADE_NOTAS = 5

for i in range (3):#(QUANTIDADE_NOTAS)
    nota += float(input("Digite uma nota: "))

media = nota / 3 #(QUANTIDADE_NOTAS)
if media >= 7:
    resultado = "Aprovado"    
elif media >= 4:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"Média: {media}")
print(f"Resultado: {resultado}")





