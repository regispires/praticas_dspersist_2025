from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine("sqlite:///meu_banco.sqlite", echo=True)
metadata = MetaData()
pessoa = Table("pessoas", metadata, autoload_with=engine)

with engine.connect() as conn:
    result = conn.execute(select(pessoa))
    for row in result:
        print(row)