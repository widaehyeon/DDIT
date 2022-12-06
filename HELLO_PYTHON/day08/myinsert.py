import psycopg2

conn = psycopg2.connect(host="localhost", dbname="python",user="postgres",password="python")
    
cur = conn.cursor()
postgres_insert_query = """ INSERT INTO sample (col01, col02, col03) VALUES (%s,%s,%s)"""
record_to_insert = ('4', '3', '3')
cur.execute(postgres_insert_query, record_to_insert)
conn.commit()
count = cur.rowcount
print(count, "Record inserted successfully into mobile table")    


cur.close()
conn.close()