import os

#Função que verifica se um número é primo ou não
def is_prime(num):
    #Essa linha se chama docstring. Serve para anotações em documentação formal.
    """Verifica se um número é primo."""
    if num <= 1:  
        return False  
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:  
            return False  
    return True  

def main():  
    primes = [num for num in range(1, 251) if is_prime(num)]  
    
    # Exibe os números primos no console  
    print("Números primos entre 1 e 250:")  
    for prime in primes:  
        print(prime)  

    # Armazena os resultados em results.txt  
    with open('results.txt', 'w') as file:  
        for prime in primes:  
            file.write(f"{prime}\n")
    
    # Obtém o diretório de trabalho atual
    current_patch = os.getcwd()

    # Constroi o caminho completo para o arquivo
    absolut_patch = os.path.join(current_patch, 'results.txt')

    #Printa no console o caminho absoluto do arquivo. Para acessá-lo no terminal, usar o cat junto ao caminho
    print(f"Absolut patch: {absolut_patch}")

if __name__ == "__main__":  
    main()