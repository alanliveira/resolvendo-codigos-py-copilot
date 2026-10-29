import pytest

from resolucoes_code.repetindo_textos import repetir_texto


def test_repete_texto_na_quantidade_informada() -> None:
    assert repetir_texto("Py", 3) == "PyPyPy"
    assert repetir_texto("Py", 0) == ""


def test_rejeita_quantidade_negativa() -> None:
    with pytest.raises(ValueError, match="não pode ser negativa"):
        repetir_texto("Py", -1)
