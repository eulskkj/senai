import os
os.system ("clear")

dia = int(input("Digite um número da semana: "))

match dia:
    case 1:
        print("Domingo") 
    case 2:
        print("Segunda-feira") 
    case 3:
        print("Terça-feira") 
    case 4:
        print("Quarta-feira") 
    case 5:
        print("Quinta-feira") 
    case 6:
        print("Sexta-feira") 
    case 7:
        print("Sabado") 
    case _:
        print("Opção inválida")






