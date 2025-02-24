import os
os.system("clear")

#elabore um algoritmo para solicitar ao usuario o login e a senha
#considere que os dados do usuario ja estao cadrastados
#caso o login e a senha estejam corretos, mostre a mensagem:
#"Bem-vindo!"
#caso contrario, mostre a mensagem:
#"login ou senha invalidos"

login_cadrastado = "marta"
senha_cadrastada = "123"

login = input ("Digite seu login: ")
senha= input("Digite sua senha: ")

if login == login_cadrastado and senha == senha_cadrastada:
    print ("Bem vindo!")
else: 
    print ("Login ou senha inválidos!")


