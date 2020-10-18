from flask import Flask, render_template, request, redirect, url_for, session
from pydblite import Base


app = Flask(__name__)
app.db = Base('users.pdl')
app.secret_key = '1234567890'


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'submitted_email' in request.form and 'submitted_password' in request.form:
            for rec in (app.db('email') == request.form['submitted_email']) and (app.db('password') == request.form['submitted_password']):
                session['loginsuccess'] = True
                return redirect(url_for('profile'))
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        if 'submitted_email' in request.form and 'submitted_password' in request.form:
            app.db.insert(email=request.form['submitted_email'],
                          password=request.form['submitted_password'])
            app.db.commit()
            return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/profile')
def profile():
    if session['loginsuccess'] == True:
        return render_template('profile.html')


@app.route('/logout')
def logout():
    if session['loginsuccess'] == True:
        session.pop('loginsuccess', None)
        return redirect(url_for('index'))

if __name__ == '__main__':
    if app.db.exists():
        app.db.open()
    else:
        app.db.create('email', 'password')
    app.run(debug=True)