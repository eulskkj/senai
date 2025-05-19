import os
os.system("clear")

primeiro_numero= float(input("digite seu numero: "))
segundo_numero= float(input("digite seu numero: "))

soma= primeiro_numero + segundo_numero
media= soma / 2

produto= primeiro_numero * segundo_numero



menor = min (primeiro_numero, segundo_numero)
maior = max (primeiro_numero, segundo_numero)


print("\nExibindo resultados: ")
print(f"Média: {media}")
print(f"produto: {produto}")
print(f"Soma: {soma}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")