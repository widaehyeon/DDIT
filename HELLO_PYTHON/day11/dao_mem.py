import psycopg2

class DaoMem:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", dbname="python",user="postgres",password="python")
        self.cur = self.conn.cursor()
    
    def selects(self):
        
        mydict = []
        self.cur.execute("select m_id, m_nm, tel, ymd from member")
        rows = self.cur.fetchall()
        for r in rows:
            mydict.append({'m_id':r[0], 'm_nm':r[1], 'tel':r[2], 'ymd':r[3]})
        return mydict
    
    def select(self, m_id):
        sql = f"""
            select 
                m_id, m_nm, tel, ymd 
            from 
                member
            where
                m_id = '{m_id}'
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        r = rows[0]
        ret = {'m_id':r[0], 'm_nm':r[1], 'tel':r[2], 'ymd':r[3]}
        return ret
    
    def insert(self, m_id, m_nm, tel, ymd ):
        sql = f"""
            insert into member
                (m_id, m_nm, tel, ymd )
            values
                ({m_id},{m_nm},{tel}, {ymd})
        """
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
    def update(self, m_id, m_nm, tel, ymd):
        
        sql = f""" 
            update member 
            set m_nm= '{m_nm}',
                tel = '{tel}',
                ymd = '{ymd}'
            where m_id='{m_id}'
            """
            
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
    def delete(self,m_id):
        sql = f""" 
            delete from member 
            where m_id='{m_id}'
            """
        
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    dm= DaoMem()
    cnt = dm.selects()
    print(cnt)
