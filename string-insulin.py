# Armazenar a sequência de preproinsulina humana em uma variável chamada proproinsulin:

preproinsulin =(
    'malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr'
    'reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn')

#Armazenar os elementos restantes da sequência da insulina humana em variáveis:

lsinsulin = ('malwmrllpllallalwgpdpaaa')

binsulin = ('fvnqhlcgshlvealylvcgergffytpkt')

cinsulin = ('giveqcctsicslyqlenycn')

ainsulin = ('rreaedlqvgqvelgggpgagslqplalegslqkr')

insulin = binsulin + ainsulin

#Exibir a sequência de insulina humana usando sucessivos comandos print():
print('A sequência da preproinsulina é:',preproinsulin)

#Mostrar no console a concatenação das strings em uma função print (linha única):
print('A sequência da insulina humana é a cadeia: ' + ainsulin)

#Calculando o peso molecular da insulina 
#Criando uma lista de peso do aminoácido (AA)
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}

#Contando o número de cada aminoácido
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']}) 

#Multiplicando a contagem pelo peso
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("O peso bruto molecular da insulina é de: " +
str((molecularWeightInsulin)))

#Cálculo do desvio
molecularWeightInsulinActual = 5807.63
print("A porcentagem da margem de erro é de: " + str(round(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100,2)))