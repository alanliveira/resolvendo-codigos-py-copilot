from resolucoes_code.calculando_media_de_notas import calcular_media


def test_calcula_media_de_tres_notas() -> None:
    assert calcular_media(7, 8, 9) == 8
