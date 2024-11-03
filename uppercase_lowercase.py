nome = input("Qual o seu nome? ").upper()

menu = input("Olá, "+ nome + ". Qual serviço gostaria de cosultar? Envio, envelope ou selo: ").lower()

if 'envio' in menu:
    print("Serviço de envio indisponível!")
elif 'envelope' in menu:
    print("Serviço de envelope indisponível")
elif 'selo' or 'selos' in menu:
    print('Serviço de selo(s) indisponível')
else:
    print("Opção inválida, tente novamente mais tarde!")