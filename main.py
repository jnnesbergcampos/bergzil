def main():
	nome = input("Qual é o seu nome? ").strip()

	try:
		idade = int(input("Qual é a sua idade? "))
	except ValueError:
		print("Digite uma idade válida usando apenas números.")
		return

	if nome:
		print(f"Olá, {nome}! A Espanha te espera!")
	else:
		print("Olá! A Espanha te espera!")

	if idade >= 18:
		print("Você é maior de idade.")
	else:
		print("Você é menor de idade.")

if __name__ == "__main__":
    main()