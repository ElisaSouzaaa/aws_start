userReply = input("Você precisa enviar um pacote? (Digite sim ou não)\n") #input equivale ao scanner do java.
print() #pula linha.
print()

#Em python, a condição não fica entre parenteses mas se usa sinal de igualdade no lugar. É necessário usar o : (dois pontos) no lugar de {} (chaves) para declarar o retorno.


#Exemplo com if/else
if userReply == "sim":
    print("Nós podemos ajudar a enviar o pacote")
else:
    print("Volte quando você precisar enviar um pacote!")