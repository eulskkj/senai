import os 
os.system ("clear")

primeiro_numero = int(input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")
segundo_numero = int(input("Digite um número: "))

match operador: 
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        resultado = "operação inválida"

print(f"\nPrimeiro número: {primeiro_numero}")
print(f"Operação: {operador}")
print(f"Segundo número: {segundo_numero}")
print(f"Resultado: {resultado}")























