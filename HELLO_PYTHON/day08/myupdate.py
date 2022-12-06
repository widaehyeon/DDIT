import psycopg2

col01 = '4'
col02 = '8'
col03 = '8'

conn = psycopg2.connect(host="localhost", dbname="python",user="postgres",password="python")
    
cur = conn.cursor()
sql = f""" 
    update sample 
    set col02= '{col02}',
        col03 = '{col03}' 
    where col01='{col01}'
    """
cur.execute(sql)
conn.commit()

count = cur.rowcount
print(count, "Record updated successfully into mobile table")    

cur.close()
conn.close()