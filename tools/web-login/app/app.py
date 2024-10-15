from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambia esto por un valor más seguro en producción

# Usuario y contraseña de ejemplo
USER_CREDENTIALS = {
    'username': 'user',
    'password': 'loveme'
}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('private'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['username'] = username
            return redirect(url_for('private'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/private')
def private():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('private.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
