"""Solução para verificar se uma palavra é um palíndromo."""


def eh_palindromo(palavra: str) -> bool:
    """Informa se a palavra é igual à sua versão invertida."""
    return palavra == palavra[::-1]


def main() -> None:
    """Lê uma palavra e informa se ela é um palíndromo."""
    palavra = input("Digite uma palavra: ")
    if eh_palindromo(palavra):
        print(f"{palavra} é um palíndromo.")
    else:
        print(f"{palavra} não é um palíndromo.")


if __name__ == "__main__":
    main()
