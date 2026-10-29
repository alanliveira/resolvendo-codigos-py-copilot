"""Solução para repetir um texto uma quantidade informada de vezes."""


def repetir_texto(texto: str, quantidade: int) -> str:
    """Repete ``texto`` exatamente ``quantidade`` vezes."""
    if quantidade < 0:
        raise ValueError("a quantidade não pode ser negativa")
    return texto * quantidade


def main() -> None:
    """Lê um texto e a quantidade de repetições."""
    texto = input("Digite um texto: ")
    quantidade = int(input("Digite a quantidade de repetições: "))
    print(repetir_texto(texto, quantidade))


if __name__ == "__main__":
    main()
