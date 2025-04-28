import os
os.system ("cls || clear")
from dataclasses import dataclass

nome = input("Digite seu nome:")
email = input("Digite seu email:")
numero = int(input("Digite seu número: "))
cidade = input("Digite sua cidade: ")
endereco = input("Digite seu endereço: ")
logradouro= input("Digite seu logradouro: ")


@dataclass
class Endereco:
    numero: str
    logradouro: str
@dataclass
class Dados:
    nome: str
    email: str
    cidade: str
    endereco: Endereco 

    def exibindo_dados(self):
        print(f"Nome: {self.nome}, E-mail: {self.email}, Cidade: {self.cidade}, Logradouro: {self.endereco.logradouro}, Endereço: {self.endereco.numero}")

endereco1 = Endereco(numero,logradouro)
pessoa1 = Dados(nome, email, cidade, endereco1)

print("=== DADOS ===")
pessoa1.exibindo_dados()