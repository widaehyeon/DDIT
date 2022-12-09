from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify
from day13.dao_student import DaoStudent

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/list', methods=['POST'])
def list():
    ds = DaoStudent()
    list = ds.selects()
    return jsonify(list = list)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    s_id = dict['s_id']
    ds = DaoStudent()
    student = ds.select(s_id)
    return jsonify(student = student)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    address = dict['address']
    
    ds = DaoStudent()
    cnt = ds.insert(s_id, s_name, mobile, address)
    list = ds.selects()
    return jsonify(list = list, cnt = cnt)

@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    dict = request.get_json()
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    address = dict['address']
    
    ds = DaoStudent()
    cnt = ds.update(s_id, s_name, mobile, address)
    list = ds.selects()
    return jsonify(list = list, cnt = cnt)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    dict = request.get_json()
    s_id = dict['s_id']

    ds = DaoStudent()
    cnt = ds.delete(s_id)
    list = ds.selects()
    return jsonify(list = list, cnt = cnt)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    