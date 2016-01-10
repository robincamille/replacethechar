# Robin Camille Davis
# CODEX 2016

# Runs index.html + nerWithInputFun.py

from flask import Flask
from flask import request
from flask import render_template
from nerWithInput import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def titleform():

    if request.method == 'GET':
        return render_template('index.html')
    else:
        title = request.form['titles']
        return render_template('index.html',
                               index=selecttext(int(title)-1))

    
if __name__ == '__main__':
    app.run(debug=True) #turn off to not get verbose messages if it breaks
