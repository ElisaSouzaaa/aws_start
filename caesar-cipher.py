# Função que dobra o alfabeto fornecido  
def getDoubleAlphabet(alphabet):  
    # Concatena o alfabeto consigo mesmo  
    doubleAlphabet = alphabet + alphabet  
    # Retorna o alfabeto duplicado  
    return doubleAlphabet  

# Função que solicita uma mensagem ao usuário  
def getMessage():  
    # Lê uma entrada do usuário que será criptografada  
    stringToEncrypt = input("Por favor, digite a mensagem a ser criptografada: \n")  
    # Retorna a mensagem inserida  
    return stringToEncrypt  

# Função que solicita a chave de cifra ao usuário  
def getCipherKey():  
    # Lê a chave de cifra (número entre 1-25) do usuário  
    shiftAmount = input("Por favor entre com a chave (números inteiros de 1-25): \n")  
    # Retorna a chave de cifra  
    return shiftAmount  

# Função que criptografa uma mensagem usando a cifra de César  
def encryptMessage(message, cipherKey, alphabet):  
    # Inicializa uma string vazia para a mensagem criptografada  
    encryptdMessage = ""  
    # Inicializa uma string para a mensagem em maiúsculas  
    uppercaseMessage = ""  
    # Converte a mensagem para letras maiúsculas  
    uppercaseMessage = message.upper()  

    # Percorre sobre cada caractere da mensagem em maiúsculas  
    for currentCharacter in uppercaseMessage:  
        # Encontra a posição do caractere no alfabeto  
        position = alphabet.find(currentCharacter)  
        # Calcula a nova posição do caractere após a aplicação da chave  
        newPosition = position + int(cipherKey)  
        # Verifica se o caractere está no alfabeto  
        if currentCharacter in alphabet:  
            # Adiciona o caractere criptografado à mensagem  
            encryptdMessage = encryptdMessage + alphabet[newPosition]  
        else:  
            # Caso contrário, adiciona o caractere original (como espaços ou pontuações)  
            encryptdMessage = encryptdMessage + currentCharacter  
    # Retorna a mensagem criptografada  
    return encryptdMessage  

# Função que descriptografa uma mensagem usando a cifra de César  
def decryptMessage(message, cipherKey, alphabet):  
    # Calcula a chave de decriptação (negativa)  
    decryptKey = -1 * int(cipherKey)  
    # Utiliza a função de criptografia para descriptografar a mensagem  
    return encryptMessage(message, decryptKey, alphabet)  

# Função principal do programa da cifra de César  
def runCaesarCipherProgram():  
    # Inicializa o alfabeto  
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    # Imprime o alfabeto  
    print(f'Alphabet: {myAlphabet}')  
    # Gera o alfabeto duplicado  
    myAlphabet2 = getDoubleAlphabet(myAlphabet)  
    # Imprime o alfabeto duplicado  
    print(f'Alphabet2: {myAlphabet2}')  
    # Solicita a mensagem do usuário  
    myMessage = getMessage()  
    # Imprime a mensagem fornecida  
    print(myMessage)  
    # Solicita a chave de cifra do usuário    
    myCipherKey = getCipherKey()  
    # Imprime a chave de cifra  
    print(myCipherKey)  
    # Criptografa a mensagem utilizando a chave e o alfabeto duplicado  
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)  
    # Imprime a mensagem criptografada  
    print(f'Encrypted Message: {myEncryptedMessage}')  
    # Descriptografa a mensagem criptografada  
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)  
    # Imprime a mensagem descriptografada  
    print(f'Decypted Message: {myDecryptedMessage}')  

# Execução do programa  
runCaesarCipherProgram()