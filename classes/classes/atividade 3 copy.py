import os
os.system ("clear || cls")

from dataclasses import dataclass

@dataclass
class Dados:
    nome: str 
    email: str
    telefone: int
    endereco: str
    def exibindo_dados(self):
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, E-mail: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}")
        

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = int(input("Digite seu número de telefone: "))
endereco = input("Digite seu endereço: ")

dados1 = Dados(nome, email, telefone, endereco)
dados1.exibindo_dados()







