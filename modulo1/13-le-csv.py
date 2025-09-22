import csv

# Leitura do arquivo CSV usando DictReader
with open("pessoas.csv", "r", newline="", encoding="utf-8") as arquivo:
	leitor = csv.DictReader(arquivo)
	
	# Exibir cada linha como dicionário
	for linha in leitor:
		print(f"Nome: {linha['nome']}, Telefone: {linha['telefone']}")
