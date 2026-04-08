# Solicita o tempo total em segundos
segundos = int(input("Digite o tempo em segundos: "))

# Calcula quantas horas existem nesse tempo
horas = segundos // 3600

# Calcula o restante após retirar as horas
resto = segundos % 3600

# Calcula os minutos a partir do resto
minutos = resto // 60

# Calcula os segundos finais restantes
segundos_restantes = resto % 60

# Exibe o tempo convertido
print("Tempo convertido:", horas, "h", minutos, "min", segundos_restantes, "s")
