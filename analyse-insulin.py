import re

with open('Lab118/preproinsulin-seq.txt', 'r') as file:
    linhas = file.readlines()

limpa_sequencia =''

for linha in linhas:
    if 'ORIGIN' in linha or '//' in linha:
        continue
    limpa_sequencia += linha.strip()

limpa_sequencia = re.sub(r'\d+','',limpa_sequencia)
limpa_sequencia = re.sub(r'\s+','',limpa_sequencia)

print(limpa_sequencia)

with open('Lab118/preproinsulin-seq-clean.txt','w') as file:
    file.write(limpa_sequencia)

lsinsulin = limpa_sequencia[:24]

with open('Lab118/lsunsulin-seq-clean.txt','w') as file:
    file.write(lsinsulin)


binsulin = limpa_sequencia[24:54]

with open('Lab118/binsulin-seq-clean.txt','w') as file:
    file.write(binsulin)


cinsulin = limpa_sequencia[54:89]

with open('Lab118/cinsulin-seq-clean.txt','w') as file:
    file.write(cinsulin)


ainsulin = limpa_sequencia[89:110]

with open('Lab118/ainsulin-seq-clean.txt','w') as file:
    file.write(ainsulin)

