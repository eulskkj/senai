import os
os.system ("clear || cls")

from dataclasses import dataclass
@dataclass
class Endereco:
    logradouro: str
    numero: str

@dataclass
class Dados:
    nome: str 
    idade: str
    endereco: Endereco

    def exibindo_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Logradouro: {self.endereco.logradouro}, Endereço: {self.endereco.numero}")
        

endereco1 = Endereco("Rua A", "33")
pessoa1 = Dados("Marta", 22 , endereco1)

print("Dados da pessoas: ")
pessoa1.exibindo_dados()







