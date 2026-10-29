"""Solução para calcular a média aritmética de três notas."""


def calcular_media(nota_1: float, nota_2: float, nota_3: float) -> float:
    """Calcula a média aritmética de três notas."""
    return (nota_1 + nota_2 + nota_3) / 3


def main() -> None:
    """Lê três notas e imprime a média."""
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    nota_3 = float(input("Digite a terceira nota: "))
    print(f"Média: {calcular_media(nota_1, nota_2, nota_3):.2f}")


if __name__ == "__main__":
    main()
