print("\n" * 130)
print("\033[36m" + "\nDesenvolvedor: Diego Lino Tome\n" + "\033[0;0m")
print("Programa: Calculadora interativa")
print("Consideracoes: Escrita em python no console 'nano' do KALI LINUX")
print("Recomendacoes: Por gentileza execute em um terminal linux de preferencia")
print("Objetivo: Resumir os conceitos raiz do Python de uma forma simples e dinamica")
print("\nObrigado a todos ja de antemao")
print("##############################################################")

print("\n=====================")
print("===== Matematica ====")
print("=====================\n")

# Variavel
decisao = 1 # Controle do loop while

# Estrutura em Loop: MENU Dinamico
while(decisao == 1):

	# Variaveis de controle quanto a logica dos calculos mediante ao Loop do MENU (Correto inicializar as variaveis)
	n1 = 0 # Entrada de valores
	n2 = 0 # Entrada de valores
	som = 0 # Soma
	sub = 0 # Subtracao
	mul = 0 # Multiplicacao
	div = 0 # Divisao
	resto = 0 # Primo
	pot = 0 # Potenciacao
	rad = 0 # Radiciacao
	perc = 0 # Porcentagem
	divr = 0 # Divisores
	fat = 0 # Fatorial

	# Variaveis de controle de fluxo de MENU
	erro = 0 # Erro na decisao
	opcao = 0 # Erro na opcao de MENU

	# MENU
	print("""--- MENU --- \n \n1.Soma \n2.Subtracao \n3.Multiplicacao \n4.Divisao \n5.Primo \n6.Potenciacao \n7.Radiciacao \n8.Porcentagem\
		\n9.Divisores \n10.Fatorial \n""")

	opcao = input("Digite a opcao desejada: ")

	# Protecao: Erros na opcao de escolha de MENU
	while(opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 7 and opcao != 8 and opcao != 9
		and opcao != 10):

		opcao = input("\nDigite a opcao desejada: ")

	# SOMA
	if(opcao == 1):

		print("\n=== Soma ===\nObs: n1 + n2\n")

		# Entrada de variaveis
		n1 = input("\033[34m" + "Digite o primeiro numero: " + "\033[0;0m")
		n2 = input("\033[33m" + "Digite o segundo numero: " + "\033[0;0m")

		# Calculo e impressao
		som = n1 + n2
		print("\033[32m" + "\nResultado: " + str(som) + "\033[0;0m")

	# SUBTRACAO
	elif(opcao == 2):

		print("\n=== Subtracao ===\nObs: n1 - n2 \n")

		# Entrada de variaveis
                n1 = input("\033[34m" + "Digite o primeiro numero: " + "\033[0;0m")
                n2 = input("\033[33m" + "Digite o segundo numero: " + "\033[0;0m")

		# Calculo
		sub = n1 - n2
		print("\033[32m" + "\nResultado: " + str(sub) + "\033[0;0m")

	# MULTIPLICACAO
	elif(opcao == 3):

		print("\n=== MULTIPLICACAO ===\nObs: n1 * n2\n")

		# Entrada de variaveis
                n1 = input("\033[34m" + "Digite o primeiro numero: " + "\033[0;0m")
                n2 = input("\033[33m" + "Digite o segundo numero: " + "\033[0;0m")

		# Calculo e Impressao
		mul = n1 * n2
		print("\033[32m" + "\nResultado: " + str(mul) + "\033[0;0m")

	# DIVISAO
	elif(opcao == 4):

		print("\n=== DIVISAO ===\nObs: n1/n2\n")

		# Entrada de variaveis
                n1 = input("\033[34m" + "Digite o primeiro numero: " + "\033[0;0m")
                n2 = input("\033[33m" + "Digite o segundo numero: " + "\033[0;0m")

		# Estrutura de Loop: Protecao contra divisao por "0"
		while(n2 == 0):
			print("\nDivisao por ZERO nao pode, pois resulta em infinito")

			# Entrada de variaveis
                	n2 = input("\033[33m" + "Digite o segundo numero: " + "\033[0;0m")

		# Calculo e Impressao
		div = n1/n2
		print("\033[32m" + "\nResultado: " + str(div) + "\033[0;0m")

	# PRIMO
	elif(opcao == 5):

		print("\n=== IDENTIFICANDO NUMEROS PRIMOS ===\n")
		n1 = input("\033[34m" + "Digite o numero: "+ "\033[0;0m")

		# Estrutura de condicao: Protecao contra numeros negativos
		if(n1 <= 0):
	 		print("\nNumero Invalido\n")

		# Estrutura de decisao: Protecao contra o numero "1"
		elif(n1 == 1):
			print("\nDivisor universal: " + str(numero) )

		else:
		   	''' 
 			Estrutura de repeticao com uma range entre "1" ate o "numero digitado"
			A range nao imprime o ultimo numero, por isso acrescenta-se mais "1"
			'''
			for contador in range( 1, (n1+1) ):
				# Estrutura condicional: Resto da divisao igual a "0"
				# Ex: numero = 89 --> Sera dividido por (1 ate (88+1) )
				if(n1 % contador == 0):
					resto += 1 # Acrescenta "1" a variavel resto

			# Numeros primos sao sempre divididos por "1" e por ele mesmo, logo terao "2" restos iguais a "0"
			if(resto == 2):
				print("\033[32m" + "\nResultado: Primo" + "\033[0;0m")

			# Caso a quantidade de restos iguais a "0" for maior que 2, nao e primo
			else:
				print("\033[32m" + "\nResultado: Nao Primo" + "\033[0;0m")

	# POTENCIACAO
	elif(opcao == 6):

		print("\n=== POTENCIACAO ===\nObs: a^(b)\n")

		# Entrada de variaveis
                n1 = input("\033[34m" + "Digite a base: " + "\033[0;0m")
                n2 = input("\033[33m" + "Digite o expoente: " + "\033[0;0m")

		# Calculo e Impressao
		pot = n1 ** n2
		print("\033[32m" + "\nResultado: " + str(pot) + "\033[0;0m")

	# RADICIACAO
	elif(opcao == 7):

		print("\n=== RADICIACAO ===\nObs: a^(1/b)\n")

		# Entrada de variaveis
                n1 = input("\033[34m" + "Digite o numero: " + "\033[0;0m")
                n2 = input("\033[33m" + "Digite a raiz: " + "\033[0;0m")

		# Calculo e Impressao(Manobra matematica de inverter o numero antes para depois o elevar, extraindo a sua raiz)
		rad = n1 ** ( n2 ** (-1) )

		print("\033[32m" + "\nResultado: " + str(rad) + "\033[0;0m")

	# PORCENTAGEM
	elif(opcao == 8):

		print("\n=== PORCENTAGEM ===\n")

                # Entrada de variaveis
                n1 = input("\033[34m" + "Digite o percentual (Sem o sinal %): " + "\033[0;0m")
                n2 = input("\033[33m" + "Digite um numero: " + "\033[0;0m")

		#Calculo e Impressao
		perc = 0.01 * n1 * n2
		print("\n \033[32m" + str(n1) + "%"  + " de " + str(n2) + " = " + str(perc) + "\033[0;0m \n")


	# DIVISORES
	elif(opcao == 9):

		print("\n=== DIVISORES ===\n")

		# Entrada de variaveis
                n1 = input("\033[34m" + "Digite o numero: " + "\033[0;0m")

		# Calculo e Impressao
		print("\n \033[32m" + "Resultados" + "\033[0;0m")

		for divisores in range(1,(n1+1)):
			if( n1 % divisores == 0 ):
				divr = str(divisores)
				print("\033[32m" + str(divr) + "\033[0;0m")

	# FATORIAL
	else:
		print("\n=== FATORIAL ===\n")

		# Entrada de variaveis
                fat = input("\033[34m" + "Digite o numero: " + "\033[0;0m")

		if(fat == 0):
			print("\033[32m" + "\nResultado: 1" + "\033[0;0m")

		else:
			for contador in range(1,fat):
				fat *= contador # fat = fat * contador (Ex: fat = fat * 1)
			print("\033[32m" + "\nResultado: " + str(fat) + "\033[0;0m")


	# Pergunta de retorno afim de mudar a condicao da estrutura while
	decisao = input("\n \033[36m" + "\nDeseja retornar ao menu anterior \n1.Sim \n2.Nao \nOpcao desejada: " + "\033[0;0m")
	print("\n" * 130)

	# Estrutura de protecao em Loop
	while( decisao != 1 and decisao != 2 ):

		print("\nERRO: " + str(erro) )
		decisao = input("\nDeseja retornar ao menu anterior \n1.Sim \n2.Nao \nOpcao desejada: ")
		print("\n" * 130)
		erro += 1 # No Python nao exite (erro++)

print("\033[42m" + "\nVolte sempre que quiser " + "\033[0;0m")
