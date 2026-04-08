# Pede um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número dividido por 2 tem resto 0
if numero % 2 == 0:
    # Se o resto for 0, é par
    print("O número é par")
else:
    # Caso contrário, é ímpar
    print("O número é ímpar")
