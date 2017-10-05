'''
Vivien Lee, Caleb Smith-Salzberg
SoftDev1 Pd7
HW07 - Do I Know You?
2017-10-04
'''

import os
from flask import Flask, render_template, request, session

app = Flask(__name__)
#generates a random 32-bit string to act as the key
app.secret_key = os.urandom(32)

@app.route('/', methods=['POST','GET'])
def login():
        return render_template('login.html', loginfailed = '')

@app.route('/login', methods=['POST'])
def checklogin():
    if request.form['user'] == 'dog':
        if request.form['pass'] == 'cat':
            session['username'] = request.form['user']
            return render_template('welcome.html', user_name = session['username'])
        else:
            return render_template('login.html', loginfailed = "Wrong password!")
    else:
        return render_template('login.html', loginfailed = "Wrong username!")


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username')
    return render_template('logout.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
