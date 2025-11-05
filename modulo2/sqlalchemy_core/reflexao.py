from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite:///meu_banco.sqlite")
metadata = MetaData()
metadata.reflect(bind=engine)
tabelas = metadata.tables

for tabela in tabelas.keys():
    print(tabela)