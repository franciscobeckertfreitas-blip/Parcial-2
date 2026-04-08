# Cria uma lista vazia
nomes = []

# Repete 5 vezes para pedir nomes
for i in range(5):
    # Solicita um nome ao usuário
    nome = input(f"Digite o {i+1}º nome: ")
    
    # Adiciona o nome na lista
    nomes.append(nome)

# Exibe mensagem inicial
print("Lista de nomes:")

# Percorre a lista e imprime cada nome
for nome in nomes:
    print(nome)
