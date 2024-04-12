import random

numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    tentativas -= 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou.")
        break

    elif palpite > numero_secreto:
        print("O seu palpite está alto.")

    elif palpite < numero_secreto:
        print("O seu palpite está baixo.")

print("Fim do jogo.")