import psycopg2


tablelist = [
    "PERSON",
    "PROVIDER",
    "VISIT_OCCURRENCE",
    "VISIT_DETAIL",
    "OBSERVATION",
    "CONDITION_OCCURRENCE",
    "DEVICE_EXPOSURE",
    "DRUG_EXPOSURE",
    "DEATH",
]

filelist = [t + ".csv" for t in tablelist]
schema = "omop_cdm"
tablelist = [schema + "." + t.lower() for t in tablelist]
try:
    conn = psycopg2.connect(
        dbname="bbmri-it-school",
        user="postgres",
        password="postgres",
        host="localhost",  # or your DB host
        port="5432",  # default PostgreSQL port
    )
except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
    exit(1)


cur = conn.cursor()


for file, table in zip(filelist, tablelist):
    try:
        with open(file, "r") as f:
            cur.copy_expert(f"COPY {table} FROM STDIN WITH CSV HEADER", f)
    except psycopg2.Error as e:
        print(f"Error copying data from {file} to {table}: {e}")
        continue

conn.commit()

cur.close()
conn.close()
