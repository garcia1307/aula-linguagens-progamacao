# Usuário digita o nome e a posição que deseja editar
nome = input("Digite seu nome: ")
posicao = int(input("Digite a posição que deseja modificar: "))

# Verificação de posição inválida
if posicao < 0 or posicao >= len(nome):
    print("Posição inválida.")
else:
    # Variável 'letra' recebe o caractere da posição selecionada pelo usuário
    letra = nome[posicao]

    # Substitui a letra com as condições seguintes
    if letra == 'r':
        nome = nome[:posicao] + 's' + nome[posicao + 1:]
    elif letra == 'm':
        nome = nome[:posicao] + 'n' + nome[posicao + 1:]
    else:
        # Deleta as letras se não sseguirem as condições
        nome = nome[:posicao] + nome[posicao + 1:]

    # Resultado do programa
    print("Nome editado:",nome)