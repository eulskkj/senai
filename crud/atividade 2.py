from dataclasses import dataclass
import time

@dataclass
class Aluno:
    nome = str
    data_de_nascimento = int
    registro_do_aluno = int
    curso = str
    endereco = str
    def exibir_dadps(self):
        print(f"Nome: {self.nome}, Data de nascimento: {self.data_de_nascimento}, R.A: {self.registro_do_aluno}, Curso: {self.curso}, Endereço: {self.endereco}")
@dataclass
class Endereco:
    logradouro = str
    numero = int
    cidade = str
    estado = str

    def exibir_dadps(self):
        print(f"Logradouro: {self.logradouro}, Número: {self.numero}, Cidade: {self.cidade}, {self.estado}")

lista_nomes = []

import os
os.system("cls || clear")

def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        return True
    return False

def adicionar_nome(lista_nomes):
    nome = input("Digite o nome que deseja adicionar: ")
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso.")

def mostrar_nomes(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\n Alista está vazia.")
        return
    print(f"- Lista nomes-")
    for nome in lista_nomes:
        print(f"- {nome}")

def excluir_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\n A lista está vazia.")
        return
    mostrar_nomes(lista_nomes)
    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover in lista_nomes:
        lista_nomes.remove(nome_remover)
        print(f"{nome_remover} foi removido com sucesso.")

def atualizar_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\n A lista está vazia.")
        return
    mostrar_nomes(lista_nomes)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_nomes:
        novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        print(f"{nome_antigo} foi atualizado para {novo_nome}.")
    else:
        print (f"\n O nome {nome_antigo}")

while True:
    print("""
    - Gerenciador de nomes -
    1 - Adicionar
    2- Listar nomes
    3- Atualizar
    4- Remover
    5- Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))
                      
    match opcao:
        case 1:
            adicionar_nome(lista_nomes)
        case 2:
            mostrar_nomes(lista_nomes)
        case 3:
            atualizar_nome(lista_nomes)
        case 4:
            excluir_nome(lista_nomes)
        case 5:
            print("Saindo do programa.")
            break
        case _:
            print("Opção inválida.")
time.sleep(5)
os.system("cls || clear")        














