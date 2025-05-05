import os
from dataclasses import dataclass
os.system("cls || clear")




@dataclass
class Autor:
    nome: str
    biografia: str
@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor
    def exibindo_dados(self):
        print(f"Nome do autor: {self.autor.nome}, Biografia do autor: {self.autor.biografia}, Titulo do livro: {self.titulo}, Ano de lançamento do livro: {self.ano} ")


lista_de_livros = []
QUANTIDADE_DE_LIVROS = 1

    

for i in range(QUANTIDADE_DE_LIVROS):
        autor = Autor(
            nome = input("Digite o nome do autor: "),
            biografia = input("Digite a biografia do autor: "))
        livro = Livro(
            titulo = input("Digite o titulo do livro: "),
            ano = int(input("Digite o ano de lançamento do livro: ")),
            autor=autor 
        )
lista_de_livros.append(livro)

print("\n= Salvando dados = ")
nome_arquivo = "dado_livros.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_livro:
    for livro in lista_de_livros:
         arquivo_livro.write(f"{livro.titulo}, {livro.ano}, {livro.autor.nome}\n")
print("\n= Dados salvoscom sucesso = ")
print("\n= Lendo dados do arquivo =")         
try:
     with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
          linhas= arquivo.readlines()
          for linha in linhas:
               print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado.")

