from sqlalchemy import create_engine, text
from conf import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

schema_name = "sql_alchemy_test"

create_schema_sql = f"CREATE SCHEMA  {schema_name}"

with engine.connect() as connection:
    connection.execute(text(create_schema_sql))
    print(f"Schema {schema_name} created")
    connection.commit()