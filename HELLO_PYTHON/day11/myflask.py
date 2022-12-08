from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day11.dao_mem import DaoMem

app = Flask(__name__)

@app.route('/')
@app.route('/mem_list')
def mem_list():
    me = DaoMem()
    list = me.selects()
    
    return render_template('mem_list.html',list=list)

@app.route('/mem_add')
def mem_add():
    return render_template('mem_add.html')

@app.route('/mem_add_act', methods=['POST'])
def mem_add_act():
    me = DaoMem()
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    cnt = me.insert(m_id, m_nm, tel, ymd)
    return render_template('mem_add_act.html', cnt=cnt)

@app.route('/mem_detail')
def mem_detail():
    me = DaoMem()
    m_id = request.args.get('m_id')
    mem = me.select(m_id)
    return render_template('mem_detail.html',mem=mem)

@app.route('/mem_edit')
def mem_edit():
    me = DaoMem()
    m_id = request.args.get('m_id')
    mem = me.select(m_id)
    return render_template('mem_edit.html',mem=mem)

@app.route('/mem_edit_act', methods=['POST'])
def mem_edit_act():
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    me = DaoMem()
    cnt = me.update(m_id, m_nm, tel, ymd)

    return render_template('mem_edit_act.html', cnt=cnt)

@app.route('/mem_delete')
def mem_delete():
    me = DaoMem()
    m_id = request.args.get('m_id')
    cnt = me.delete(m_id)
    return render_template('mem_delete.html',cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    