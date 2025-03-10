import os
os.system("clear")

matricula = input("Digite a matricula do empregado: ")
idade = int(input("Digite a idade do empregado: ")) 
tempo_de_trabalho = int(input("Digite o tempo de trabalho empregado: "))


idade = 2025 - idade
if idade >- 65 and tempo_de_trabalho >- 30:
    resultado = "Requer aposentadoria"
else:
    resultado = "Não requerer aposentaodria"

print(f"\nMatricula: {matricula}")
print(f"Idade: {idade}")
print(f"Tempo de trabalho: {tempo_de_trabalho}")
print(f"Resultado: {resultado}")

