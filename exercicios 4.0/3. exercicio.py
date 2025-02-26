import os
os.system ("clear")






idade = int(input("Digite sua idade: "))


if idade < 18 or idade > 65:
    resultado = "Não é obrigadoto a votar"
else:
    resultado = "Voto obrigatório"


print(f"\nResultado: {resultado}")