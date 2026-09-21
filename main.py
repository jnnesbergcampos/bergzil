def main():
	nome = input("Qual é o seu nome? ").strip()
    idade = int(input("Qual é a sua idade? "))

	if nome:
		print(f"Olá, {nome}! A espanha te espera")
    if idade > 18:
        print("Você é maior de idade.")
    if idade < 18:
        print("Você é menor de idade.")
	else:
		print("Olá! a espanha te espera")


if __name__ == "__main__":
	main()