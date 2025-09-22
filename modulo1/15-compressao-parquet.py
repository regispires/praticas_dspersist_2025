import pandas as pd
import time, os

# Cria DataFrame simples (ajuste N para mais impacto)
N = 5_000_000
df = pd.DataFrame({
	"id": range(N),
	"valor": [f"texto_{i}" for i in range(N)]
})
# Compressões a testar
compressions = ["snappy", "gzip", "zstd", "lz4", None]
tempos = []
for comp in compressions:
	fname = f"dados_{comp or 'none'}.parquet"
	
	# mede tempo
	t0 = time.perf_counter()
	df.to_parquet(fname, engine="pyarrow", compression=comp, index=False)
	elapsed = time.perf_counter() - t0
	
	size = os.path.getsize(fname)
	
	tempos.append({
		"compressao": comp or "none",
		"tempo_segundos": round(elapsed, 3),
		"tamanho_MB": round(size / (1024*1024), 2)
	})
# Mostra resultados
resultado = pd.DataFrame(tempos)
print(resultado)
