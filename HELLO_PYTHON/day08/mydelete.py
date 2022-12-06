import psycopg2

col01 = '4'

conn = psycopg2.connect(host="localhost", dbname="python",user="postgres",password="python")
    
cur = conn.cursor()
sql = f""" 
    delete from sample 
    where col01='{col01}'
    """
cur.execute(sql)
conn.commit()

count = cur.rowcount
print(count, "Record deleted successfully into mobile table")    

cur.close()
conn.close()