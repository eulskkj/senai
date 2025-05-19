#Foi feita uma pesquisa entre os habitantes de uma região.  Foram coletados os dados de idade, sexo (M/F) e salário. 
#Faça um algoritmo que informe:  
#a) a média de salário do grupo;
#b) maior e menor idade do grupo;
#c) quantidade de mulheres com salário a partir de R$ 5.000,00.
#Crie um menu com três opções.
#Código |   Descrição
#1        |   Adicionar pessoa
#2       |   Exibir resultados
#3       |   Sair
#O final da leitura de dados se dará com quando o usuário digitar o número código 3. 
#Ao adicionar uma pessoa, deve-se limpar o terminal e apresentar o menu novamente.

import os
os.system("cls || clear")

contador = 0
soma = 0
salario_feminino = 0
idades = []






while True:
    # Mostrando o menu
    tabela = int(input(""" 
    Código | Descrição
       1   |  Adicionar pessoa   
       2   |  Exibir resultados  
       3   |  Sair  
Digite sua opção desejada: """))
    
    match tabela:
        case 1:
            # Pedindo dados
            salario = float(input("Digite o salário: "))
            sexo = input("Digite seu sexo (M/F): ").strip().lower()
            idade = int(input("Digite sua idade: "))

            # Armazena a idade na lista
            idades.append(idade)

            # Conta mulheres com salário >= 5000
            if sexo == "f" and salario >= 5000:
                salario_feminino += 1

            # Atualiza soma dos salários e contador de pessoas
            soma += salario
            contador += 1

        case 2:
            if contador > 0:
                media = soma / contador
            else:
                media = 0

            if idades:  # Garante que há idades registradas antes de usar max() e min()
                print(f"Maior idade: {max(idades)}")
                print(f"Menor idade: {min(idades)}")
            else:
                print("Nenhuma idade registrada.")

            print(f"Média salarial: R$ {media:.2f}")
            print(f"Quantidade de mulheres com salário >= R$5.000: {salario_feminino}")
            
            input("\nPressione Enter para continuar...")

        case 3:
            print("Finalizando programa...")
            break

        case _:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")
















