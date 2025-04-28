import os
os.system("cls || clear")
#adicionando classes
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float
#pedindo dados
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

pessoa1= Pessoa(nome=nome, idade=idade, peso=peso, altura=altura)
pessoa2= Pessoa(nome, idade, peso, altura)
#mostrando dados
print("=== DADOS ===")
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade} anos, Peso: {pessoa1.peso} KG, Altura: {pessoa1.altura} m")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade} anos, Peso: {pessoa2.peso} KG, Altura: {pessoa2.altura} m")
















