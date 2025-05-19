import os 
os.system("cls || clear")


#Faça um algoritmo que mostre um menu com
#opções de um cardápio de restaurante para
#uma pessoa. A pessoa vai escolher o prato
#desejado.

#Após escolher o prato, o algoritmo deve
#perguntar ao usuário se ele deseja escolher
#outro prato.

#Quando o usuário não quiser mais realizar
#pedidos, mostre o nome e o valor dos pratos
#escolhidos e calcule o valor  total da conta

pratos_escolhidos = []
total = 0


while True:
    menu = float(input("""
                   
CÓDIGO|      PRATO       |      VALOR
   1  |     PICANHA      |     R$ 25     
   2  |     LASANHA      |     R$ 20
   3  |    STROGONOFF    |     R$ 18
   4  |  BIFE ACEBOLADO  |     R$ 15
   5  |   PÃO COM OVO    |     R$ 5

Digite um código de  seu pedido: """))

    match menu:
        case 1:
            nome = "Picanha"
            valor = 25
        case 2:
            nome = "Lasanha"
            valor = 20
        case 3:
            nome = "Strogonoff"
            valor = 18
        case 4:
            nome = "Bife acebolado"
            valor = 15
        case 5:
            nome = "Pão com ovo"
            valor = 5
        case _:
            print("Opção inválida")
            continue
        #armazenando os valores
    total += valor
    pratos_escolhidos.append(f"{valor} - {nome}")

        #Pedindo outros pratos 
    outro_pedido = input("Deseja pedir algo mais? (digite 0 caso não queira ou pressione enter para continuar): ")  

        #Terminando o pedido
    if outro_pedido == "0":
        break
#exibindo resultados
print("\n=== RESUMO DO PEDIDO ===")
print("Pratos escolhidos:")
for prato in pratos_escolhidos:
    print(prato)
print (f"Valor final: R${total:.2f}")
print(f"Obrigado pela preferência e um bom apetite.")
