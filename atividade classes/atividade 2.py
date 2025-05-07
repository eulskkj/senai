import os
from dataclasses import dataclass
os.system("cls || clear")


@dataclass
class Cliente:
    nome: str
    data_nascimento: int
    endereco: str
    def exibir_dados(self):
        print(f"Nome: {self.nome},Data de nascimento: {self.data_nascimento},Endereço: {self.endereco} ")
@dataclass
class Funcionario:
    nome: str
    data_admissao: int
    matricula: int
    endereco: str 
    def exibir_dados(self):
        print(f"Nome: {self.nome}, Data de admissão: {self.data_admissao}, Matricula: {self.matricula},Endereço: {self.endereco} ")

lista_clientes = []
QUANTIDADE_CLIENTE = 2

for i in range(QUANTIDADE_CLIENTE):
    dados_cliente = Cliente(
        nome = input("Nome do cliente: "),
        data_nascimento = int(input("Data de nascimento do cliente: ")),
        endereco = input("Digite o endereço do cliente: ")
    )
    os.system("cls || clear")
    lista_clientes.append(dados_cliente)

nome_arquivo_cliente = "DADOS_CLIENTE.txt"
with open (nome_arquivo_cliente, "a", encoding="utf-8") as arquivo_cliente:
    for dado_cliente in lista_clientes:
        arquivo_cliente.write(f"Nome do cliente: {dado_cliente.nome},Data de nascimento do cliente:  {dado_cliente.data_nascimento}, Endereço do cliente: {dado_cliente.endereco}\n") 

lista_funcionario = []
QUANTIDADE_FUNCIONARIO = 2

for i in range(QUANTIDADE_FUNCIONARIO):
    dados_funcionario = Funcionario(
        nome = input("Nome do funcionario: "),
        data_admissao = int(input("Data de admissão do funcionario: ")),
        matricula = int(input("Digite a matricula do funcionario: ")),
        endereco = input("Digite o endereço do funcionario: ")
    )
    os.system("cls || clear")
    lista_funcionario.append(dados_funcionario)
nome_arquivo_funcionario ="DADOS_FUNCIONARIO.txt"
with open (nome_arquivo_funcionario, "a", encoding="utf-8") as arquivo_funcionario:
    for dado_funcionario in lista_funcionario:
        arquivo_funcionario.write(f"Nome do funcionário: {dado_funcionario.nome}, Data de admissão do funcionário: {dado_funcionario.data_admissao}, Matricula do funcionário: {dado_funcionario.matricula}, Endereço do funcionário: {dado_funcionario.endereco}\n")





