userReply = input("Você gostaria de comprar um selo, comprar um envelope ou fazer uma cópia?(Digite selo, envelope ou cópia)\n") #input equivale ao scanner do java.
print() #pula linha.
print()

#Em python, a condição não fica entre parenteses mas se usa sinal de igualdade no lugar. É necessário usar o : (dois pontos) no lugar de {} (chaves) para declarar o retorno.


#Exemplo com if/elif/else

# if userReply == "selo":
#     print("Nós temos muitos modelos de selos para escolher!")
# elif userReply == "envelope":
#     print("Nós temos vários tamanos de envelope para escolher")
# elif userReply == "cópia":
#     copias = input("Quantas cópias gostaria de fazer?(Escolha um número)\n")
#     print("Aqui está {} cópias.".format(copias))
# else:
#     print("Resposta inválida!")

if userReply == "selo":
    print("Nós temos muitos modelos de selos para escolher!")
elif userReply == "envelope":
    print("Nós temos vários tamanos de envelope para escolher")
elif userReply == "cópia":
    copias = input("Quantas cópias gostaria de fazer?(Escolha um número)\n")
    print("Aqui está",copias,"cópias. Volte sempre!")
else:
    print("Resposta inválida! Obrigada e até a próxima!")