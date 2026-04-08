# Solicita o capital inicial
capital = float(input("Digite o capital inicial: "))

# Solicita a taxa de juros (em porcentagem)
taxa = float(input("Digite a taxa de juros (%): "))

# Solicita o tempo
tempo = float(input("Digite o tempo: "))

# Calcula o valor dos juros simples
juros = capital * (taxa / 100) * tempo

# Calcula o montante final (capital + juros)
montante = capital + juros

# Mostra o valor dos juros
print("Juros:", juros)

# Mostra o valor total final
print("Montante final:", montante)
