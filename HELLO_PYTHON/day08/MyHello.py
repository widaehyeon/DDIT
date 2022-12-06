from flask import Flask
from flask.globals import request
from day09.dao_sample import DaoSample
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'
    
@app.route('/param')
def param():
    a = request.args.get('a','babo')
    return 'param:' + a

@app.route('/post', methods=['POST'])
def post():
    a = request.form['a']
    return 'post:' + a

@app.route('/sample')
def sample():
    
    ds = DaoSample()
    list = ds.selects()
    
    return str(list)

@app.route('/view')
def view():

    a = "홍길동"
    b = ["바보", "천재", "미남"]
    c = [
        {'col01':'1', 'col02':'1', 'col03':'1'},
        {'col01':'2', 'col02':'2', 'col03':'2'},
    ]
    
    return render_template('view.html',a=a, b=b, c=c)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    