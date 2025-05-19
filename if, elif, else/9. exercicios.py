import os
os.system ("clear")

#labore um algoritmo para solicitar ao usuário o login e a senha.
#onsidere que os dados do usuário já estão cadastrados.
#Caso o login e senha estejam corretos, mostre a mensagem:
 #“Bem-vindo!”
#Caso contrário, mostre a mensagem: 
#“Login ou senha inválidos.”

login_cadrastada= "Catia"
senha_cadrastada= "123"

login= input("Digite seu login: ")
senha= input("Digite sua senha: ")

if login == login_cadrastada and senha == senha_cadrastada:
    print ("Bem-vindo!")
else:
    print ("Login ou senha inválidos")    



