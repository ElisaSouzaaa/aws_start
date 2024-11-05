print("Bem-vindo ao jogo 'Adivinhe o Número'!\nAs regras são simples. Eu vou pensar em um número e você tentará adivinhar qual é.")

import random

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Escolha um número de  à 10: ")
    if int(guess) == number:
        print("Você chutou {}. E está correto! Você ganhou!".format(guess))
        isGuessRight = True
    else:
        print("Você chutou {}. E está incorreto! Tente novamente.".format(guess))

