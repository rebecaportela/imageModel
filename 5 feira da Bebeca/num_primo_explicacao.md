# Verificador de Números Primos - Explicação para Iniciantes

## 📝 O que é um Número Primo?

Um **número primo** é um número natural maior que 1 que possui exatamente dois divisores: **1 e ele mesmo**.

### Exemplos:
- **2** é primo (divisores: 1, 2)
- **3** é primo (divisores: 1, 3)
- **4** NÃO é primo (divisores: 1, 2, 4 - tem 3 divisores!)
- **5** é primo (divisores: 1, 5)
- **17** é primo (divisores: 1, 17)

---

## 🛠️ Explicação do Código

### 1. **Docstring do Módulo**

```python
"""
Módulo para verificação de números primos.

Este módulo contém funções para determinar se um número é primo.
Um número primo é aquele que só é divisível por 1 e por ele mesmo.
"""
```

A **docstring** é um comentário especial que explica o que o arquivo faz. Está entre **três aspas** `"""` e aparece no início.

---

### 2. **Função `is_prime()`**

```python
def is_prime(number: int) -> bool:
```

#### Partes importantes:

- `def` = define uma nova função
- `is_prime` = nome da função (significa "é primo" em inglês)
- `number: int` = o parâmetro se chama `number` e deve ser um **inteiro** (`int`)
- `-> bool` = a função **retorna** um valor booleano (`True` ou `False`)

#### O que a função faz:

A função recebe um número e **retorna `True`** se é primo ou **`False`** se não é.

---

### 3. **Verificação 1: Números Menores ou Iguais a 1**

```python
if number <= 1:
    return False
```

**Por quê?** Por definição matemática, números menores ou iguais a 1 **não são primos**.

- `-5` → não é primo ✗
- `0` → não é primo ✗
- `1` → não é primo ✗

---

### 4. **Verificação 2: O Número 2**

```python
if number == 2:
    return True
```

**Por quê?** O número **2 é o único número primo par**. Todos os outros números pares são divisíveis por 2, então não podem ser primos.

---

### 5. **Verificação 3: Números Pares Maiores que 2**

```python
if number % 2 == 0:
    return False
```

- `%` = operador de **resto da divisão** (módulo)
- `number % 2 == 0` significa "o resto da divisão por 2 é zero"
- O resultado é **False** porque qualquer número par (além do 2) **não é primo**

Exemplos:
- `4 % 2 = 0` → 4 é par → não é primo
- `100 % 2 = 0` → 100 é par → não é primo

---

### 6. **Verificação 4: Divisibilidade até a Raiz Quadrada**

```python
for divisor in range(3, int(number**0.5) + 1, 2):
    if number % divisor == 0:
        return False
```

Esta é a **parte mais importante e eficiente**! Vamos entender cada parte:

#### O que significa `range(3, int(number**0.5) + 1, 2)`?

- `3` = começa a verificar a partir de 3
- `number**0.5` = calcula a **raiz quadrada** do número
  - Exemplo: `9**0.5 = 3`, `16**0.5 = 4`, `25**0.5 = 5`
- `+ 1` = adiciona 1 para incluir a raiz quadrada na verificação
- `2` = pula de 2 em 2 (só testa números **ímpares**, porque já testamos os pares)

#### Por que até a raiz quadrada?

**Regra matemática importante:** Se um número `n` tem um divisor maior que sua raiz quadrada, ele **obrigatoriamente** tem um divisor menor que sua raiz quadrada.

**Exemplo com número 36:**
- Raiz quadrada de 36 = 6
- Divisores de 36: 1, 2, 3, 4, 6, 9, 12, 18, 36
- Se `36 % 9 = 0` (9 é divisor), então `36 % 4 = 0` também (4 é divisor)
- **Conclusão:** não precisamos verificar além de 6!

Isso torna o algoritmo muito mais **rápido** porque testamos muito menos divisores.

#### O que o `for` faz?

```python
for divisor in range(3, int(number**0.5) + 1, 2):
    if number % divisor == 0:
        return False
```

- Testa cada número **ímpar** de 3 até a raiz quadrada
- Se encontrar um número que divide perfeitamente (resto = 0), o número **não é primo**
- Retorna `False` imediatamente

**Exemplo com 17:**
- Raiz quadrada de 17 ≈ 4.1
- Testa: 3
- `17 % 3 = 2` (não divide)
- Nenhum divisor encontrado
- Retorna `True` (é primo!)

---

### 7. **Retorno Final**

```python
return True
```

Se passou por todas as verificações sem encontrar divisores, o número **é primo**!

---

### 9. **Função `get_number_from_user()`**

```python
def get_number_from_user() -> int:
```

Esta função faz comunicação com o usuário. Vamos entender cada parte:

#### O que faz:

```python
while True:
    try:
        number = int(input("\nDigite um número inteiro para verificar se é primo: "))
        return number
    except ValueError:
        print("❌ Erro! Por favor, digite um número inteiro válido.")
```

- **`while True:`** = cria um loop infinito que continua pedindo até o usuário fornecer uma entrada válida
- **`input()`** = função que para a execução e espera o usuário digitar algo
- **`int()`** = converte o texto digitado em um número inteiro
- **`try/except`** = estrutura de tratamento de erros:
  - `try` = tenta executar o código
  - `except ValueError` = se o usuário digitar algo que não é número, aparece a mensagem de erro
- **`return number`** = retorna o número válido

#### Por que usar `try/except`?

Sem essa proteção, se o usuário digitasse "abc" ao invés de um número, o programa **travaria** com um erro. Com `try/except`, o programa **continua funcionando** e pede novamente.

**Exemplo de execução:**
```
Digite um número inteiro para verificar se é primo: abc
❌ Erro! Por favor, digite um número inteiro válido.
Digite um número inteiro para verificar se é primo: 17
```

---

### 10. **Função `interactive_check()`**

```python
def interactive_check() -> None:
```

Esta é a função **principal**, que conecta tudo! Ela:

1. Exibe um menu visual com separadores
2. Pede o número ao usuário
3. Verifica se é primo
4. Mostra o resultado de forma amigável

#### Código da função:

```python
def interactive_check() -> None:
    """
    Função interativa que solicita ao usuário um número e verifica se é primo.
    """
    print("=" * 50)              # Desenha uma linha de =
    print("🔍 VERIFICADOR DE NÚMEROS PRIMOS")
    print("=" * 50)
    
    number = get_number_from_user()  # Pede número ao usuário
    result = is_prime(number)        # Verifica se é primo
    
    # Exibe o resultado de forma amigável
    if result:
        print(f"\n✅ {number} é um número PRIMO!")
    else:
        print(f"\n❌ {number} NÃO é um número primo.")
    
    print("=" * 50)
```

#### O que você vê ao executar:

```
==================================================
🔍 VERIFICADOR DE NÚMEROS PRIMOS
==================================================

Digite um número inteiro para verificar se é primo: 17

✅ 17 é um número PRIMO!
==================================================
```

ou

```
==================================================
🔍 VERIFICADOR DE NÚMEROS PRIMOS
==================================================

Digite um número inteiro para verificar se é primo: 20

❌ 20 NÃO é um número primo.
==================================================
```

---

### 11. **O Bloco `if __name__ == "__main__":`**

```python
if __name__ == "__main__":
    interactive_check()
```

**O que significa?**

Quando você executa o arquivo diretamente (não importa de outro arquivo), Python define uma variável especial chamada `__name__` com o valor `"__main__"`.

- Se você executa `python num_primo.py` → `__name__ == "__main__"` é **True** → executa `interactive_check()`
- Se outro arquivo importa este arquivo → `__name__` tem outro valor → não executa

**Por quê é útil?**

Permite que você use as funções em outros programas sem executar `interactive_check()` automaticamente:

```python
# Em outro arquivo Python
from num_primo import is_prime

# Usa a função sem executar o menu interativo
print(is_prime(17))  # True
```

---

```python
def test_is_prime() -> None:
```

Esta função executa vários testes para validar se a função `is_prime()` está funcionando corretamente.

#### Lista de testes:

```python
test_cases = [
    (2, True),      # 2 é primo
    (3, True),      # 3 é primo
    (4, False),     # 4 não é primo
    (17, True),     # 17 é primo
    (1, False),     # 1 não é primo
    (0, False),     # 0 não é primo
    (-5, False),    # números negativos não são primos
    (97, True),     # 97 é primo
    (100, False),   # 100 não é primo
]
```

Cada teste é um **par** (tupla) com:
1. Um número para testar
2. O resultado esperado

#### Loop de testes:

```python
for number, expected in test_cases:
    result = is_prime(number)
    status = "✓ PASSOU" if result == expected else "✗ FALHOU"
    print(f"is_prime({number:3d}) = {str(result):5s} | Esperado: {str(expected):5s} | {status}")
```

- Testa cada número
- Compara o resultado com o esperado
- Mostra ✓ (passou) ou ✗ (falhou)
- Usa **formatação especial** para deixar bonito:
  - `{number:3d}` = número com 3 espaços
  - `{str(result):5s}` = resultado com 5 espaços

---

## 🎯 Técnicas de Clean Code Aplicadas

1. **Type Hints** (`-> bool`, `number: int`) - deixa claro o tipo da entrada e saída
2. **Docstrings** - documentação clara do que cada função faz
3. **Nomes descritivos** - `is_prime` é mais claro que `p`, `number` é mais claro que `n`
4. **Variáveis significativas** - `divisor` explica o propósito, não `i`
5. **Comentários úteis** - explicam *por quê*, não *o quê*
6. **Função de testes** - valida o código automaticamente
7. **Otimização** - pula números pares, verifica até raiz quadrada
8. **Formatação** - código bem indentado e organizado
9. **Tratamento de erros** - usa `try/except` para validar entrada do usuário
10. **Separação de responsabilidades** - cada função tem um propósito específico:
    - `is_prime()` apenas verifica se é primo
    - `get_number_from_user()` apenas pede número ao usuário
    - `interactive_check()` coordena o fluxo da aplicação
11. **Interface amigável** - usa emojis e formatação para melhorar a experiência do usuário
12. **Reutilização de código** - `interactive_check()` reutiliza as outras funções

---

## 🚀 Como Usar

### Opção 1: Teste Automatizado (Validação)

```python
python num_primo.py
```

Este comando executará a função `interactive_check()` que pedirá um número ao usuário e verificará se é primo.

### Opção 2: Usar a Função Diretamente no Código

```python
# Testar um número específico
print(is_prime(17))  # True
print(is_prime(20))  # False
```

---

## 🛡️ Tratamento de Erros

Uma diferença importante entre aplicações profissionais e scripts simples é o **tratamento de erros**.

### Sem tratamento de erros (❌ Ruim):
```python
number = int(input("Digite um número: "))
print(is_prime(number))
```

Se o usuário digitar "abc", o programa **trava**:
```
Digite um número: abc
Traceback (most recent call last):
  File "num_primo.py", line X, in <module>
    number = int(input("Digite um número: "))
ValueError: invalid literal for int() with base 10: 'abc'
```

### Com tratamento de erros (✅ Bom):
```python
try:
    number = int(input("Digite um número: "))
except ValueError:
    print("❌ Erro! Por favor, digite um número válido.")
```

Agora o programa **continua funcionando** e pede novamente!

---

## 📊 Fluxo do Programa

```
INÍCIO
  ↓
Executa interactive_check()
  ↓
Exibe menu visual
  ↓
Chama get_number_from_user()
  ├→ Pede número ao usuário
  ├→ Validação do input (try/except)
  ├→ Se inválido, pede novamente
  └→ Se válido, retorna o número
  ↓
Chama is_prime(number)
  └→ Verifica se é primo
  ↓
Exibe resultado com emojis
  ↓
FIM
```

---

## 💻 Exemplos de Execução

### Exemplo 1: Testando o número 17 (Primo)

```
==================================================
🔍 VERIFICADOR DE NÚMEROS PRIMOS
==================================================

Digite um número inteiro para verificar se é primo: 17

✅ 17 é um número PRIMO!
==================================================
```

### Exemplo 2: Testando o número 20 (Não primo)

```
==================================================
🔍 VERIFICADOR DE NÚMEROS PRIMOS
==================================================

Digite um número inteiro para verificar se é primo: 20

❌ 20 NÃO é um número primo.
==================================================
```

### Exemplo 3: Usuário digita um valor inválido

```
==================================================
🔍 VERIFICADOR DE NÚMEROS PRIMOS
==================================================

Digite um número inteiro para verificar se é primo: abc
❌ Erro! Por favor, digite um número inteiro válido.
Digite um número inteiro para verificar se é primo: 2

✅ 2 é um número PRIMO!
==================================================
```

Como você vê, mesmo quando o usuário erra digitando "abc", o programa **não trava**. Ele pede novamente até receber uma entrada válida!

---

---

## 📚 Conceitos Importantes para Iniciantes

| Conceito | Explicação |
|----------|-----------|
| **Função** | Um bloco de código reutilizável que faz uma tarefa específica |
| **Parâmetro** | O valor que a função recebe |
| **Retorno** | O resultado que a função devolve |
| **Booleano** | Um valor que é `True` ou `False` |
| **Módulo** | Um resto da divisão |
| **Raiz quadrada** | O número que, multiplicado por si mesmo, dá o original |
| **Loop** | Um bloco de código que se repete |
| **Docstring** | Documentação escrita dentro do código |
| **Try/Except** | Estrutura para tratar erros sem deixar o programa travar |
| **Type Hints** | Anotações que indicam o tipo de dados esperado |
| **Input** | Função que pede dados ao usuário |
| **Validação** | Verificar se os dados fornecidos são válidos |

---

## ✅ Conclusão

Esta função é uma ótima exemplo de como escrever código **eficiente**, **legível** e **bem documentado**. Ela demonstra que não precisamos apenas resolver o problema, mas devemos fazê-lo de forma elegante e com boas práticas de programação!
