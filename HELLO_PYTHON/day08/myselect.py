import psycopg2

conn = psycopg2.connect(host="localhost", dbname="python",user="postgres",password="python")
    
cur = conn.cursor()
cur.execute("select col01,col02,col03 from sample")
rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()
conn.close()