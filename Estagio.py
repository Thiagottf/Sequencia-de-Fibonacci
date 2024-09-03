def is_fibonacci_number(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

def count_letter_a(s):
    return s.lower().count('a')

def calculate_soma():
    INDICE = 12
    SOMA = 0
    K = 0
    while K < INDICE:
        K += 1
        SOMA += K
    return SOMA

def find_next_in_sequence():
    sequences = {
        'a': [1, 3, 5, 7],  # Resposta: 7 (soma dos ímpares)
        'b': [2, 4, 8, 16, 32],  # Resposta: 64 (multiplicação por 2)
        'c': [0, 1, 4, 9, 16, 25],  # Resposta: 36 (quadrados perfeitos)
        'd': [1, 1, 2, 3, 5],  # Resposta: 8 (sequência de Fibonacci)
        'e': [2, 10, 12, 16, 17, 18],  # Resposta: 19 (diferença crescente)
    }
    next_elements = {
        'a': 7,
        'b': 64,
        'c': 36,
        'd': 8,
        'e': 19,
    }
    return next_elements

def lamp_solution():
    return (
        "Ligue o primeiro interruptor e espere um tempo.\n"
        "Desligue o primeiro interruptor e ligue o segundo.\n"
        "Vá até a sala:\n"
        "- A lâmpada acesa é controlada pelo segundo interruptor.\n"
        "- A lâmpada quente mas apagada é controlada pelo primeiro interruptor.\n"
        "- A lâmpada fria e apagada é controlada pelo terceiro interruptor."
    )

def main():
    # 1. Sequência de Fibonacci
    num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if is_fibonacci_number(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

    # 2. Contagem da letra 'a' em uma string
    string = input("Informe uma string para verificar a quantidade de 'a': ")
    count = count_letter_a(string)
    print(f"A letra 'a' ocorre {count} vezes na string.")

    # 3. Valor da variável SOMA
    soma = calculate_soma()
    print(f"O valor de SOMA após o processamento é {soma}.")

    # 4. Próximos elementos nas sequências
    next_elements = find_next_in_sequence()
    for seq, next_elem in next_elements.items():
        print(f"O próximo elemento na sequência {seq} é {next_elem}.")

    # 5. Solução do problema dos interruptores e lâmpadas
    print(lamp_solution())

if __name__ == "__main__":
    main()
