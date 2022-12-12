from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify
import time

app = Flask(__name__)

@app.route('/')
@app.route('/three')
def three():
    return render_template('three.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    