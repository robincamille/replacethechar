# Robin Camille Davis
# CODEX 2016

# Runs index.html + nerWithInputFun.py

from flask import Flask
from flask import request
from flask import render_template
from nerWithInput import *

app = Flask(__name__)

#this works to send title info to the names.html page
@app.route('/', methods=['GET', 'POST'])
def titleform():
    if request.method == 'GET':
        return render_template('index.html')
    else: # POST
        title = request.form['titles']
        return render_template('names.html',
                               titlechosen = selecttext(int(title)-1))


#currently does not render names :(
@app.route('/names', methods=['GET', 'POST'])
def nameform(titlechosen, names = None):
    if request.method == 'GET':
        #names = printnames(titlechosen)
        #names = ['God', 'James', 'Christ', 'Almighty', 'Call']
        names = 'It me' 
        return render_template('names.html', names = names)
    else: # POST
        #title = request.form['names']
        nameschosen = request.form['nameschosenform']
        return render_template('end.html', nameschosen)


#finish form page is not done
#input nameschosen, output downloadable text
@app.route('/finish', methods=['GET', 'POST'])
def finishform(nameschosen, namesOfPpl = None):
    if request.method == 'GET':
        finishfile = outputfile(nameschosen)
        return render_template('finish.html', finishfile)

    
if __name__ == '__main__':
    app.run(debug=True) #turn off to not get verbose messages if it breaks
