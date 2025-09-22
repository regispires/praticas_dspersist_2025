import csv

# Dados de exemplo
pessoas = [
	{"nome": "Ana Silva", "telefone": "(85) 99999-1111"},
	{"nome": "João Souza", "telefone": "(88) 98888-2222"},
	{"nome": "Maria Oliveira", "telefone": "(88) 97777-3333"}
]

# Criação do arquivo CSV
with open("pessoas.csv", "w", newline="", encoding="utf-8") as arquivo:
	escritor = csv.DictWriter(arquivo, fieldnames=["nome", "telefone"])
	
	# Escreve o cabeçalho
	escritor.writeheader()
	
	# Escreve os dados
	for pessoa in pessoas:
		escritor.writerow(pessoa)