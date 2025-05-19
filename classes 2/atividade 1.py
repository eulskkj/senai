import os
from dataclasses import dataclass
os.system("cls || clear")


@dataclass
class Dados:
    nome: str
    data_nascimento: float
    rg: int
    cpf: int

    def exibindo_dados(self):
        print(f"Nome: {self.nome},Data denascimento: {self.data_nascimento}, RG: {self.rg}, CPF: {self.cpf} ")
lista_dados =[]   
QUANIDADE_DADOS = 1

for i in range(QUANIDADE_DADOS):
    dados = Dados(
    nome = input("Digite o nome da pessoa: "),
    data_nascimento = input("Digite a data de nascimeno da pessoa: "),
    rg = input("Digite o RG da pessoa: "),
    cpf = input("Digite o CPF da pessoa: ")
    )
lista_dados.append(dados)

nome_aquivo = "DADOS.txt"
with open (nome_aquivo, "a", encoding="utf-8") as arquivo:
    for dado in lista_dados:
        arquivo.write(f"{dado.nome}, {dado.data_nascimento}, {dado.rg}, {dado.cpf}")
try:
    with open(nome_aquivo, "r", encoding="utf-8") as arquivos:
        linhas = arquivos.readline()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado")