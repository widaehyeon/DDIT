from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify
from day12.dao_emp import DaoEmp

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    de = DaoEmp()
    list = de.selects()
    return jsonify(list = list)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    e_id = dict['e_id']
    de = DaoEmp()
    emp = de.select(e_id)
    return jsonify(emp = emp)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    e_id = dict['e_id']
    e_name = dict['e_name']
    sex = dict['sex']
    addr = dict['addr']
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, sex, addr)
    list = de.selects()
    return jsonify(list = list, cnt = cnt)

@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    dict = request.get_json()
    e_id = dict['e_id']
    e_name = dict['e_name']
    sex = dict['sex']
    addr = dict['addr']
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, sex, addr)
    list = de.selects()
    return jsonify(list = list, cnt = cnt)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    dict = request.get_json()
    e_id = dict['e_id']

    de = DaoEmp()
    cnt = de.delete(e_id)
    list = de.selects()
    return jsonify(list = list, cnt = cnt)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    