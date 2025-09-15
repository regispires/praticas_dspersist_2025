import sys
# Abrir o arquivo para escrita
with open("arquivo2.txt", "w") as file:
    # Ler do teclado até o fim da entrada
    for linha in sys.stdin:
        file.write(linha)
