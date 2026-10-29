import pytest

from resolucoes_code.operacoes_matematicas_simples import calcular


@pytest.mark.parametrize(
    ("operacao", "esperado"),
    [("1", 12), ("2", 4), ("3", 32), ("4", 2)],
)
def test_calcula_operacoes_matematicas(operacao: str, esperado: float) -> None:
    assert calcular(8, 4, operacao) == esperado


def test_rejeita_divisao_por_zero() -> None:
    with pytest.raises(ValueError, match="dividir por zero"):
        calcular(8, 0, "4")
