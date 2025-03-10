import os
os.system("clear")

valor_do_produto= float(input("Digite o valor do produto: "))
forma_de_pagamento= int(input(""" 
1- A vista
2- A prazo                                                            
Digite a forma de pagamento:  """))


match forma_de_pagamento:
    case 1:
        desconto = valor_do_produto * 0.10
        valor_pagar = valor_do_produto - desconto

        print(f"\nValor do produto: {valor_do_produto}")
        print(f"\nForma de pagamento: á vista")
        print(f"Valor do desconto: {desconto}")
        print(f"Total a pagar: {valor_pagar}")
    case 2:
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        if quantidade_parcelas >= 1 and quantidade_parcelas <= 1:
            valor_parcela = valor_do_produto / quantidade_parcelas

            print(f"\nValor do produto: {valor_do_produto}")
            print(f"Forma de pagamento: à prazo")
            print(f"\nQuantidade de parcelas: {quantidade_parcelas}")
            print(f"\nValor por parcela: {valor_parcela}")
            print(f"Total à prazo: R$ {valor_do_produto}")
        else:
            print(f"O parcelamento deve ser em até 6 parcelas. ")
    case _:
        print("Opção inválida")     





