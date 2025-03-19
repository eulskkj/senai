import os
os.system ("cls || clear")

#Crie um programa que solicite ao usuário seu login e
#uma senha. 
#O programa deve continuar pedindo o login e a senha
#até que ambos estejam corretos


login_cadrastado = "luis"
senha_cadrastada = "1234"


while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login_cadrastado == login and senha_cadrastada == senha:
        print("Acesso permitido!")
        break
    else: 
        print("Senha ou login inválidos!")
        











