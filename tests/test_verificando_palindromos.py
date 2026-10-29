from resolucoes_code.verificando_palindromos import eh_palindromo


def test_verifica_palindromos() -> None:
    assert eh_palindromo("arara") is True
    assert eh_palindromo("python") is False
