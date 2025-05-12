class Aluno:
    def __init__(self, nome, data_nascimento, ra, curso, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.ra = ra
        self.curso = curso
        self.endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nR.A.: {self.ra}\nCurso: {self.curso}\nEndereço: {self.endereco}"

def criar_aluno(alunos):
    print("\n--- Cadastrar Novo Aluno ---")
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    ra = input("R.A.: ")
    curso = input("Curso: ")
    print("\n--- Endereço ---")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    endereco = {"Logradouro": logradouro, "Número": numero, "Cidade": cidade, "Estado": estado}
    aluno = Aluno(nome, data_nascimento, ra, curso, endereco)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def ler_alunos(alunos):
    if not alunos:
        print("\nNão há alunos cadastrados.")
        return
    print("\n--- Lista de Alunos ---")
    for aluno in alunos:
        print(aluno)
        print("-" * 20)

def atualizar_aluno(alunos):
    if not alunos:
        print("\nNão há alunos cadastrados para atualizar.")
        return
    ra_busca = input("\nDigite o R.A. do aluno que deseja atualizar: ")
    for i, aluno in enumerate(alunos):
        if aluno.ra == ra_busca:
            print("\n--- Dados Atuais do Aluno ---")
            print(aluno)
            print("\n--- Digite os Novos Dados (deixe em branco para manter o valor atual) ---")
            novo_nome = input(f"Novo Nome ({aluno.nome}): ") or aluno.nome
            nova_data_nascimento = input(f"Nova Data de Nascimento ({aluno.data_nascimento}): ") or aluno.data_nascimento
            novo_curso = input(f"Novo Curso ({aluno.curso}): ") or aluno.curso
            print("\n--- Novo Endereço ---")
            novo_logradouro = input(f"Novo Logradouro ({aluno.endereco['Logradouro']}): ") or aluno.endereco['Logradouro']
            novo_numero = input(f"Novo Número ({aluno.endereco['Número']}): ") or aluno.endereco['Número']
            nova_cidade = input(f"Nova Cidade ({aluno.endereco['Cidade']}): ") or aluno.endereco['Cidade']
            novo_estado = input(f"Novo Estado ({aluno.endereco['Estado']}): ") or aluno.endereco['Estado']
            novo_endereco = {"Logradouro": novo_logradouro, "Número": novo_numero, "Cidade": nova_cidade, "Estado": novo_estado}

            alunos[i] = Aluno(novo_nome, nova_data_nascimento, ra_busca, novo_curso, novo_endereco)
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno com R.A. não encontrado.")

def deletar_aluno(alunos):
    if not alunos:
        print("\nNão há alunos cadastrados para deletar.")
        return
    ra_busca = input("\nDigite o R.A. do aluno que deseja deletar: ")
    for i, aluno in enumerate(alunos):
        if aluno.ra == ra_busca:
            del alunos[i]
            print("Aluno deletado com sucesso!")
            return
    print("Aluno com R.A. não encontrado.")

def exibir_menu():
    print("\n--- Menu ---")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Deletar Aluno")
    print("5. Sair")

def main():
    alunos = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_aluno(alunos)
        elif opcao == '2':
            ler_alunos(alunos)
        elif opcao == '3':
            atualizar_aluno(alunos)
        elif opcao == '4':
            deletar_aluno(alunos)
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()