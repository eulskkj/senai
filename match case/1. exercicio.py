import os
os.system ("clear")


opcao = int(input("""
Código \t Prato \t\t Valor
                  
1 \t picanha \t R$25,00
                  
2 \t Lasanha \t R$ 20,00
                                                                      
3 \t Strogonoff \t R$ 18,00
                  
4 \t Bife acebolado\t R$ 15,00
                  
5 \t Pão com ovo \t R$5,00
                                   
Digite a opção desejada:
"""))

match opcao:
    case 1:
        print("Picanha - R$ 25,00")
    case 2:
        print("Lasanha - R$20,00")
    case 3:
        print("Strogonoff - R$ 18,00")
    case 4:
        print("Bife_acebolado - R$15,00")
    case 5:
        print("Pão_com_ovo - R$ 5,00")
    case _: 
        "Opção inválida"
print(f"Opção: {opcao}")






