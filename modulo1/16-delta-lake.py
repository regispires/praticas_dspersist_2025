import pandas as pd
from deltalake import DeltaTable, write_deltalake, WriterProperties

path = "data/my_delta_rs"
wp = WriterProperties(compression="zstd")

# 1) CREATE (overwrite) com dados iniciais
df = pd.DataFrame({
	"id": [1, 2, 3],
	"nome": ["Ana", "Bruno", "Carla"],
	"idade":[29, 33, 27],
})
write_deltalake(path, df, mode="overwrite", writer_properties=wp)

# 2) INSERT (append)
df_new = pd.DataFrame({"id":[4], "nome":["Diego"], "idade":[31]})
write_deltalake(path, df_new, mode="append", writer_properties=wp)

# 3) READ
dt = DeltaTable(path)
df = dt.to_pyarrow_table().to_pandas()
print(df)