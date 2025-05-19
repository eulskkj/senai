import os
os.system("clear")
#exemplo de estrutura conditicional anilhada
#Match-case substitui o uso do if-elif-else

dia = input("Digite dia da semana: ")
match dia:
    case "Segunda":
        print("Hoje é segunda-feira!")
    case "Terça":
        print("Hoje é terça-feira!")
    case "Quarta":
        print("Hoje é quarta-feira!")
    case "Quinta":
        print("Hoje é segunda-feira!")
    case "Sexta":
        print("Hoje é sexta-feira!")
    case "Sabado":
        print("Hoje é sabado!")
    case "Domingo":
        print("Hoje é domingo!")
    case _:
        print("Dia inválido")

print(dia)
print("=== FIM ===")
