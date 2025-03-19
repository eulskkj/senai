import os 
os.system ("cls || clear")





soma = 0

for i in range (3):
    nota = float(input("Digite uma nota: "))
    soma += nota
media = soma / 3
if media >= 7:
    resultado = "Aprovado"    
elif media >= 4:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"Média: {media}")
print(f"Resultado: {resultado}")





