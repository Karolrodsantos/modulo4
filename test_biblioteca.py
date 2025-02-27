import pytest
from biblioteca import adicionar_livro, remover_livro, consultar_disponibilidade, livros, emprestimos

def test_adicionar_livro():
    global livros
    livros.clear()
    def test_adicionar_livro():
        global livros
        livros.clear()
        adicionar_livro("Livro Teste", "Autor Teste", "1234567890")
        assert len(livros) == 1
        assert livros[0]["titulo"] == "Livro Teste"
        assert livros[0]["autor"] == "Autor Teste"
        assert livros[0]["isbn"] == "1234567890"

    def test_remover_livro():
        global livros
        livros.clear()
        livros.append({"titulo": "Livro Teste", "autor": "Autor Teste", "isbn": "1234567890"})
        remover_livro("1234567890")
        assert len(livros) == 0

    def test_consultar_disponibilidade():
        global emprestimos
        emprestimos.clear()
        emprestimos.append({"id_usuario": "1", "isbn": "1234567890"})
        assert not consultar_disponibilidade("1234567890")
        assert consultar_disponibilidade("0987654321")

    def test_registrar_usuario():
        global usuarios
        usuarios.clear()
        registrar_usuario("Usuario Teste", "1")
        assert len(usuarios) == 1
        assert usuarios[0]["nome"] == "Usuario Teste"
        assert usuarios[0]["id"] == "1"

    def test_registrar_emprestimo():
        global emprestimos
        emprestimos.clear()
        registrar_emprestimo("1", "1234567890")
        assert len(emprestimos) == 1
        assert emprestimos[0]["id_usuario"] == "1"
        assert emprestimos[0]["isbn"] == "1234567890"
    assert consultar_disponibilidade("0987654321")