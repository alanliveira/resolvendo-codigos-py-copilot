"""Solução para operações matemáticas básicas entre dois números."""


OPERACOES = {
    "1": ("soma", lambda primeiro, segundo: primeiro + segundo),
    "2": ("subtração", lambda primeiro, segundo: primeiro - segundo),
    "3": ("multiplicação", lambda primeiro, segundo: primeiro * segundo),
    "4": ("divisão", lambda primeiro, segundo: primeiro / segundo),
}


def calcular(primeiro_numero: float, segundo_numero: float, operacao: str) -> float:
    """Calcula a operação identificada por ``operacao`` entre dois números."""
    opcao = OPERACOES.get(operacao)
    if opcao is None:
        raise ValueError("operação inválida")
    if operacao == "4" and segundo_numero == 0:
        raise ValueError("não é possível dividir por zero")
    return opcao[1](primeiro_numero, segundo_numero)


def main() -> None:
    """Exibe um menu de operações e imprime o resultado escolhido."""
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
    operacao = input("Escolha a operação: ").strip()
    print(calcular(primeiro_numero, segundo_numero, operacao))


if __name__ == "__main__":
    main()
