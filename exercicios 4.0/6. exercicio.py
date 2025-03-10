import os
os.system ("clear")

altura = float(input("Digite sua altura: "))
sexo = input("Informe seu gênero (M para masculino ou F para feminino: ): ").upper()

match sexo:
    case "M":
        resultado = 72.7 * altura - 58
        print(f"Peso ideal: {resultado:.2f}")
    case "F":
        resultado = 62.1 * altura - 58        
        print(f"Peso ideal: {resultado:.2f}")
    case _:
        print("Operação inválida")




