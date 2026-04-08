# Solicita o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação (+, -, *, /): ")

# Verifica qual operação foi escolhida
if operacao == "+":
    resultado = num1 + num2  # Soma
elif operacao == "-":
    resultado = num1 - num2  # Subtração
elif operacao == "*":
    resultado = num1 * num2  # Multiplicação
elif operacao == "/":
    # Evita divisão por zero
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    # Caso a operação não seja válida
    resultado = "Operação inválida"

# Mostra o resultado
print("Resultado:", resultado)
