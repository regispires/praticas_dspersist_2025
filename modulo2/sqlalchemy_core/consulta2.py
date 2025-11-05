from sqlalchemy import create_engine, MetaData, Table, select
from datetime import date

engine = create_engine("sqlite:///meu_banco.sqlite", echo=True)
metadata = MetaData()
pessoa = Table("pessoas", metadata, autoload_with=engine)

stmt = select(pessoa).where(pessoa.c.dt_nasc > date(1990, 1, 1))
with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(row.nome, row.dt_nasc)