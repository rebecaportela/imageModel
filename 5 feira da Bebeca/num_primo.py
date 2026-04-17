"""
Módulo para verificação de números primos.

Este módulo contém funções para determinar se um número é primo.
Um número primo é aquele que só é divisível por 1 e por ele mesmo.
"""


def is_prime(number: int) -> bool:
    """
    Verifica se um número é primo.
    
    Args:
        number: Um número inteiro para verificar se é primo.
        
    Returns:
        bool: True se o número é primo, False caso contrário.
        
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
    # Números menores ou iguais a 1 não são primos por definição
    if number <= 1:
        return False
    
    # 2 é o único número primo par
    if number == 2:
        return True
    
    # Números pares maiores que 2 não são primos
    if number % 2 == 0:
        return False
    
    # Verifica divisibilidade até a raiz quadrada do número
    # Se n tem um divisor maior que sqrt(n), terá também um menor
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    
    return True


def test_is_prime() -> None:
    """
    Executa testes para validar a função is_prime.
    """
    test_cases = [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (1, False),
        (0, False),
        (-5, False),
        (97, True),
        (100, False),
    ]
    
    print("Executando testes da função is_prime...\n")
    
    for number, expected in test_cases:
        result = is_prime(number)
        status = "✓ PASSOU" if result == expected else "✗ FALHOU"
        print(f"is_prime({number:3d}) = {str(result):5s} | Esperado: {str(expected):5s} | {status}")
    
    print("\nTodos os testes concluídos!")


def get_number_from_user() -> int:
    """
    Solicita um número ao usuário via terminal.
    
    Returns:
        int: O número inteiro fornecido pelo usuário.
        
    Raises:
        ValueError: Se o usuário não fornecer um número válido.
    """
    while True:
        try:
            number = int(input("\nDigite um número inteiro para verificar se é primo: "))
            return number
        except ValueError:
            print("❌ Erro! Por favor, digite um número inteiro válido.")


def interactive_check() -> None:
    """
    Função interativa que solicita ao usuário um número e verifica se é primo.
    """
    print("=" * 50)
    print("🔍 VERIFICADOR DE NÚMEROS PRIMOS")
    print("=" * 50)
    
    number = get_number_from_user()
    result = is_prime(number)
    
    # Exibe o resultado de forma amigável
    if result:
        print(f"\n✅ {number} é um número PRIMO!")
    else:
        print(f"\n❌ {number} NÃO é um número primo.")
    
    print("=" * 50)


if __name__ == "__main__":
    interactive_check()
