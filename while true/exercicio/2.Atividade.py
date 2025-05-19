import os
os.system ("clear || cls")
#Faça um algoritmo que mostre um menu com
#opções de um cardápio de restaurante para
#uma pessoa. A pessoa vai escolher o prato
#desejado.
#Após escolher o prato, o algoritmo deve
#perguntar ao usuário se ele deseja escolher
#outro prato.
#Calcule quanto deve ser pago pelo cliente.

total = 0

while True:
    codigo = int(input(""" 
 CÓDIGO    PRATO         VALOR        
   1      PICANHA       R$25,00                                      
   2      LASANHA       R$20,00
   3     STROGONOFF     R$18,00 
   4   BIFE ACEBOLADO   R$15,00         
   5    PÃO COM OVO     R$5,00        

Digite o código do seu pedido:
"""))       
    match codigo:
        case 1:
            valor = 25
        case 2:
            valor = 20
        case 3:
            valor = 18
        case 4:
            valor = 15
        case 5:
            valor = 5
        case _:
            print("Opção inválida")
        
    total += valor
    outro_pedido = input("Deseja pedir algo mais? (S para sim e N para não): ").lower()    
    if outro_pedido == "N":
        print(f"Total: {total}")
        break
















