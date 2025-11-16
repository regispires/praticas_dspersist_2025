from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///meu_banco.sqlite", echo=True)

with engine.connect() as conn:
    result = conn.execute(text('select * from pessoas'))
    for row in result:
        print(row)