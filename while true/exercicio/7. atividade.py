import os
os.system("cls || clear")


#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados
#sobre o salário e número de filhos das famílias da cidade. A prefeitura deseja saber:  
#a) total de famílias que responderam a pesquisa;
#b) média do salário da população;
#c) média do número de filhos;
#d) maior salário;
#e) menor salário.
#Crie um menu com duas opções.
#Código |   Descrição
#     1         |   Adicionar família
#     2        |   Sair e exibir resultados
#O final da leitura de dados se dará com quando o usuário digitar o número código 2. 


contador = 0
soma = 0
soma2 = 0
salarios = []






while True:
    # Mostrando o menu
    tabela = int(input(""" 
   Código |   Descrição
     1    |   Adicionar família
     2    |   Sair e exibir resultados
                       
Digite sua opção desejada: """))
    
    match tabela:
        case 1:
            # Pedindo dados
            salario = float(input("Digite o salário: "))
            filhos = int(input("Digite a quantidade de filhos(a): "))
            contador += 1
            # Armazena a salario na lista
            salarios.append(salario)

            # media de salarios
            soma += salario

            #media de filhos
            soma2 += filhos
            import os
            os.system("cls || clear")
        case 2:
            #calcula media salarial e media de filhos
            if contador > 0:
                media = soma / contador
                media_filhos = soma2 / contador
            else:
                media = 0

            # Garante que há salarios registrados
            if salario:  
                print(f"Maior salario: {max(salarios)}")
                print(f"Menor salario: {min(salarios)}")
            else:
                print(f"Média salarial: R$ {media:.2f}")
            print(f"Media de filhos: {media_filhos:.2f}")
            print(f"Total de familia que respondeu: {contador}")
            input("\nPressione Enter para continuar...")
            print("Nenhuma salario registrado.")
            import os
            os.system("cls || clear")

        case _:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")









