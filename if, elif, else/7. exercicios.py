import os
os.system("clear")

#Elabore um algoritmo usando operações lógicas para ler 3 números e escrever:
#Os 3 números informados.
#O maior número;
#O menor número; 

primeiro_numero=float(input("Digite seu numero: "))
segundo_numero=float(input("Digite seu numero: "))
terceiro_numero=float(input("Digite seu numero: "))

menor = min(primeiro_numero, segundo_numero, terceiro_numero)
maior = max(primeiro_numero, segundo_numero, terceiro_numero)

print(f"Primeiro numero: {primeiro_numero}")
print(f"Segundo numero: {segundo_numero}")
print(f"Terceiro numero: {terceiro_numero}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")
if primeiro_numero==segundo_numero==terceiro_numero:
    print("Numeros são iguais")
else:
    print(f"Menor: {menor}")
    print(f"Maior: {maior}")
