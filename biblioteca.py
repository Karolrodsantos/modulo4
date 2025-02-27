livros = []
usuarios = []
emprestimos = []

def adicionar_livro(titulo, autor, isbn):
    global livros
    livros.append({"titulo": titulo, "autor": autor, "isbn": isbn})

def remover_livro(isbn):
    global livros
    livros = [livro for livro in livros if livro["isbn"] != isbn]

def listar_livros():
    global livros
    for livro in livros:
        print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, ISBN: {livro["isbn"]}')

def registrar_usuario(nome, id_usuario):
    global usuarios
    usuarios.append({"nome": nome, "id": id_usuario})

def listar_usuarios():
    global usuarios
    for usuario in usuarios:
        print(f'Nome: {usuario["nome"]}, ID: {usuario["id"]}')

def registrar_emprestimo(id_usuario, isbn):
    global emprestimos
    emprestimos.append({"id_usuario": id_usuario, "isbn": isbn})

def consultar_disponibilidade(isbn):
    global emprestimos
    for emprestimo in emprestimos:
        if emprestimo["isbn"] == isbn:
            return False
    return True

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Listar Livros")
        print("4. Registrar Usuário")
        print("5. Registrar Empréstimo")
        print("6. Consultar Disponibilidade de Livro")
        print("0. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            isbn = input("ISBN do Livro: ")
            adicionar_livro(titulo, autor, isbn)
        elif opcao == 2:
            isbn = input("ISBN do Livro a ser removido: ")
            remover_livro(isbn)
        elif opcao == 3:
            listar_livros()
        elif opcao == 4:
            nome = input("Nome do Usuário: ")
            id_usuario = input("ID do Usuário: ")
            registrar_usuario(nome, id_usuario)
        elif opcao == 5:
            id_usuario = input("ID do Usuário: ")
            isbn = input("ISBN do Livro: ")
            registrar_emprestimo(id_usuario, isbn)
        elif opcao == 6:
            isbn = input("ISBN do Livro: ")
            if consultar_disponibilidade(isbn):
                print("Livro disponível.")
            else:
                print("Livro emprestado.")
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()