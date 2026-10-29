"""Solução para identificar se um número inteiro é par ou ímpar."""


def verificar_paridade(numero: int) -> str:
    """Retorna ``par`` para números pares e ``ímpar`` nos demais casos."""
    return "par" if numero % 2 == 0 else "ímpar"


def main() -> None:
    """Lê um número inteiro e informa sua paridade."""
    numero = int(input("Digite um número inteiro: "))
    print(f"O número {numero} é {verificar_paridade(numero)}.")


if __name__ == "__main__":
    main()
