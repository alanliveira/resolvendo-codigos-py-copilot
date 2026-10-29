from resolucoes_code.concatenando_dados import concatenar_dados


def test_concatena_dois_dados() -> None:
    assert concatenar_dados("Olá, ", "mundo!") == "Olá, mundo!"
