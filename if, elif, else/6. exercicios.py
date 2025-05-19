import os
os.system("clear")

#Exercícios
#Elabore um algoritmo usando operações lógicas para solicitar ao
#usuário 2 números e escrever:
#Os 2 números informados.
#O maior número;
#O menor número; 

primeiro_numero= float(input("Digite seu numero: "))
segundo_numero= float(input("Digite seu numero: "))

menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)

print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Primeiro numero: {primeiro_numero}")
print(f"Segundo numero: {segundo_numero}")
