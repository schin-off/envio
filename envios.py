def dimensoesObjeto(): #a função das dimensões
   while True: #um looping pra poder usar o try e except
        try:
            altura = float(input("Qual a altura da encomenda?(em cm) ")) #as perguntar pra saber sobre a altura, comprimento e largura
            comprimento = float(input("Qual o comprimento da encomenda?(em cm) "))
            largura = float(input("Qual a largura da encomenda?(em cm) "))

            volume = altura * comprimento * largura #a formula
            print(f"O volume do objeto é: {volume} cm³\n")

            #os ifs pra poder retornar o valor certo
            if volume < 1000:
                return 10
            elif volume >= 1000 and volume < 10000:
                return 20
            elif volume >= 10000 and volume < 30000:
                return 30
            elif volume >= 30000 and volume < 100000:
                return 50
            elif volume >= 100000: # caso passe do limite
                print("Dimensões excedem o valor maximo!\nDigite as dimensões necessarias novamente!\n")
        except ValueError: #caso não digitem um valor numerico
            print("Digite valores numéricos para as dimensões do objeto.")

def pesoObjeto(): #a função do peso
    while True:
        try:
            peso = float(input("Qual o peso da encomenda?(em kg) ")) #a pergunta para saber do peso
            print(f"O peso da encomenda é: {peso} kg\n")

            #os ifs para retornar o valor certo
            if peso <= 0.1:
                return 1
            elif peso >= 0.1 and peso < 1:
                return 1.5
            elif peso >= 1 and peso < 10:
                return 2
            elif peso >= 10 and peso < 30:
                return 3
            elif peso >= 30: #caso exceda o peso maximo
                print("Peso excede o limite aceito!\nDigite um valor novamente!")
        except ValueError: #caso coloque um valor não numerico
            print("Digite valores numéricos para o peso do objeto.")

def rotaObjeto(): #a função da rota
    while True:
        try: #as rotas
            print(f"Estas são nossas rotas disponiveis!\n{'='*36}\nRS - De Rio de Janeiro até São Paulo \nSR - De São Paulo até Rio de Janeiro \nBS - De Brasília até São Paulo \nSB - De São Paulo até Brasília \nBR - De Brasília até Rio de Janeiro \nRB - Rio de Janeiro até Brasília\n{'='*36}")
            rota = input("Qual a rota desejada? ").upper() #esse .upper() pra caso digite em minusculo alguma letra, não de um erro
            print(f"A rota escolhida foi: {rota}\n")

            #os ifs para saber que valor retornar
            if rota == "RS" or rota == "SR":
                return 1
            elif rota == "BS" or rota == "SB":
                return 1.2
            elif rota == "BR" or rota == "RB":
                return 1.5
            else: #caso coloque um valor invalido
                print("Rota invalida, tente novamente!\n")
        except ValueError:
            print("Algo deu errado, tente novamente!") #este except está apenas por precaução, mas acredito quer não tenha como dar algum erro nesta parte

print("Bem vindo a companhia de logistica do Gabriel Schinoff!") #a identificação

#pegando os valores de cada função
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

#calculando os valores
valorFinal = dimensoes * peso * rota

#o resultado final
print(f"O total a ser pago é: R${valorFinal:.2f} (dimensões: {dimensoes} * peso: {peso} * rota: {rota})")
input()