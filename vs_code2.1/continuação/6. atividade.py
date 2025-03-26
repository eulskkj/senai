import os
os.system ("cls || clear")

#continuar

contador = 0
soma = 0
salario_feminino = 0

while True:
    tabela = int(input(""" 
    Código | Descrição
       1   |  Adicionar pessoa   
       2   |  Exibir resultados  
       3   |  Sair  
Digite sua opção desejada: """))
    
    match tabela:
        case 1:
            salario = float(input("Digite o salário: "))
            idade = int(input("Digite sua idade: "))
            sexo = input("Digite seu sexo (M/F): ")
            contador += 1
        case 2:
            print(f"Media salarial: {media}")
            print(f"Quantidade de salário feminino a partir de R$5.000: {salario_feminino}")
            print(f"Maior idade: {maior}")
            print(f"Menor idade: {menor}")
        case 3:
            break 
        case _:
            print("opção inválida")

            salario += soma
            media = soma / contador
            menor = min(idade)
            maior = max(idade)
            salario_feminino == "F" and salario_feminino == 5.000


















