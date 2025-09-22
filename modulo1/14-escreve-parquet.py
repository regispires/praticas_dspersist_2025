import pandas as pd

# Criando um DataFrame simples
df = pd.DataFrame({
	"nome": ["Ana", "Bruno", "Carlos"],
	"idade": [23, 30, 27],
	"cidade": ["Fortaleza", "São Paulo", "Recife"]
})

# Salvando em formato Parquet
df.to_parquet("dados.parquet", engine="pyarrow", compression="zstd", index=False)

# Lendo o arquivo Parquet
df_lido = pd.read_parquet("dados.parquet", engine="pyarrow")

print(df_lido)
