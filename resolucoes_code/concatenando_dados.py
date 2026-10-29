"""Solução para concatenar dois dados de texto."""


def concatenar_dados(primeiro_dado: str, segundo_dado: str) -> str:
    """Une dois valores de texto sem alterar o conteúdo informado."""
    return primeiro_dado + segundo_dado


def main() -> None:
    """Lê dois dados e exibe a concatenação."""
    primeiro_dado = input("Digite o primeiro dado: ")
    segundo_dado = input("Digite o segundo dado: ")
    print(concatenar_dados(primeiro_dado, segundo_dado))


if __name__ == "__main__":
    main()
