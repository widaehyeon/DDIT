import psycopg2

class DaoEmp:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", dbname="python",user="postgres",password="python")
        self.cur = self.conn.cursor()
    
    def selects(self):
        
        mydict = []
        self.cur.execute("select e_id, e_name, sex, addr from emp order by 1")
        rows = self.cur.fetchall()
        for r in rows:
            mydict.append({'e_id':r[0], 'e_name':r[1], 'sex':r[2], 'addr':r[3]})
        return mydict
    
    def select(self, e_id):
        sql = f"""
            select 
                e_id, e_name, sex, addr 
            from 
                emp
            where
                e_id = '{e_id}'
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        r = rows[0]
        ret = {'e_id':r[0], 'e_name':r[1], 'sex':r[2], 'addr':r[3]}
        return ret
    
    def insert(self, e_id, e_name, sex, addr):
        sql = f"""
            insert into emp
                (e_id, e_name, sex, addr)
            values
                ({e_id},{e_name},{sex}, {addr})
        """
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
    def update(self, e_id, e_name, sex, addr):
        
        sql = f""" 
            update emp 
            set e_name= '{e_name}',
                sex = '{sex}',
                addr = '{addr}'
            where e_id='{e_id}'
            """
            
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
    def delete(self,e_id):
        sql = f""" 
            delete from emp 
            where e_id='{e_id}'
            """
        
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    de= DaoEmp()
    cnt = de.selects()
    print(cnt)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    