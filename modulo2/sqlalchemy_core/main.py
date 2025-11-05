from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, insert
from datetime import date

engine = create_engine("sqlite:///meu_banco.sqlite", echo=True)
metadata = MetaData()
pessoas = Table("pessoas", metadata,
    Column("id", Integer, primary_key=True),
    Column("nome", String(50), nullable=False),
    Column("dt_nasc", Date, nullable=False),
    Column("fone", String(11))
)
metadata.create_all(engine)
with engine.begin() as conn:
    conn.execute(
        insert(pessoas),
        [
            {"nome": "João", "dt_nasc": date(1995, 4, 12), "fone": "88999998888"},
            {"nome": "Maria", "dt_nasc": date(1990, 8, 23), "fone": "85912345678"},
            {"nome": "José", "dt_nasc": date(1988, 1, 3), "fone": "85987654321"},
        ],
    )
print("Tabela criada e dados inseridos com sucesso!")