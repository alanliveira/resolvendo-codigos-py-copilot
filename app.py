"""Menu interativo para executar as soluções dos exercícios."""

from collections.abc import Callable

from resolucoes_code import (
    calculando_media_de_notas,
    concatenando_dados,
    operacoes_matematicas_simples,
    repetindo_textos,
    verificando_numeros_pares_impares,
    verificando_palindromos,
)


SOLUCOES: dict[str, tuple[str, Callable[[], None]]] = {
    "1": ("Concatenando Dados", concatenando_dados.main),
    "2": ("Repetindo Textos", repetindo_textos.main),
    "3": ("Operações Matemáticas Simples", operacoes_matematicas_simples.main),
    "4": (
        "Verificando Números Pares e Ímpares",
        verificando_numeros_pares_impares.main,
    ),
    "5": ("Calculando Média de Notas", calculando_media_de_notas.main),
    "6": ("Verificando Palíndromos", verificando_palindromos.main),
}


def exibir_menu() -> None:
    """Exibe as opções disponíveis."""
    print("\n=== Resoluções em Python ===")
    for numero, (titulo, _) in SOLUCOES.items():
        print(f"{numero} - {titulo}")
    print("0 - Sair")


def main() -> None:
    """Executa o menu até que a pessoa usuária escolha sair."""
    while True:
        exibir_menu()
        escolha = input("Escolha uma solução: ").strip()

        if escolha == "0":
            print("Até logo!")
            return

        solucao = SOLUCOES.get(escolha)
        if solucao is None:
            print("Opção inválida. Tente novamente.")
            continue

        print(f"\n--- {solucao[0]} ---")
        try:
            solucao[1]()
        except ValueError as erro:
            print(f"Entrada inválida: {erro}")


if __name__ == "__main__":
    main()
