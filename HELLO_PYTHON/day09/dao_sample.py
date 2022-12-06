import psycopg2

class DaoSample:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", dbname="python",user="postgres",password="python")
        self.cur = self.conn.cursor()
    
    def selects(self):
        
        mydict = []
        self.cur.execute("select col01, col02, col03 from sample")
        rows = self.cur.fetchall()
        for r in rows:
            mydict.append({'col01':r[0], 'col02':r[1], 'col03':r[2]})
        return mydict
    
    def select(self, col01):
        sql = f"""
            select 
                col01, col02, col03 
            from 
                sample
            where
                col01 = '{col01}'
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        r = rows[0]
        ret = {'col01':r[0], 'col02':r[1], 'col03':r[2]}
        return ret
    
    def insert(self, col01, col02, col03):
        sql = f"""
            insert into sample
                (col01, col02, col03)
            values
                ({col01},{col02},{col03})
        """
        self.cur.execute(sql)
        self.conn.commit()
        count = self.cur.rowcount
        return count
    
    def update(self, col01, col02, col03):
        
        sql = f""" 
            update sample 
            set col02= '{col02}',
                col03 = '{col03}' 
            where col01='{col01}'
            """
            
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
    def delete(self,col01):
        sql = f""" 
            delete from sample 
            where col01='{col01}'
            """
        
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    ds= DaoSample()
    cnt = ds.delete('4')
    print(cnt)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    