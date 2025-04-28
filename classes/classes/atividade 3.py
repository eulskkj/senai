import os
os.system ("clear || cls")

from dataclasses import dataclass

@dataclass
class Dados:
    nome: str 
    email: str
    telefone: int
    endereco: str

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = int(input("Digite seu número de telefone: "))
endereco = input("Digite seu endereço: ")
dados1 = Dados(nome, email, telefone, endereco)

print(f"Nome: {dados1.nome}, E-mail: {dados1.email}, Telefone: {dados1.telefone}, Endereço: {dados1.endereco}")







