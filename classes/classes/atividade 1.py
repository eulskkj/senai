import os
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    etnia: str
@dataclass
class Pet:
    nome: str
    idade: int
    raca: str

pessoa1= Pessoa("Alice", 30, "Indigena")
pessoa2= Pessoa("Bob", 25, "Pardo")

pet1 = Pet("Toto", 4, "Pastor alemao")
pet2 = Pet("Hulk", 5, "Pitbull")

print("=== DADOS ===")
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Etnia: {pessoa1.etnia}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}, Etnia: {pessoa2.etnia}")

print(f"Nome: {pet1.nome}, Idade: {pet1.idade}, Raça: {pet1.raca}")
print(f"Nome: {pet2.nome}, Idade: {pet2.idade}, Raça: {pet2.raca}")


