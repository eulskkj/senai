import os
os.system ("cls || clear")

soma = 0

for i in range(3):
    nota = float(input("Digite sua nota: "))
    soma += nota
media = soma / 4
if media >= 7:
    situacao = "Aprovado!"
else:
    situacao = "Reprovado!"

print()
print(f"Media: {media}")
print(f"Situação: {situacao}")
print(f"FIM DO PROGRAMA")





