from resolucoes_code.verificando_numeros_pares_impares import verificar_paridade


def test_identifica_paridade() -> None:
    assert verificar_paridade(24) == "par"
    assert verificar_paridade(-3) == "ímpar"
