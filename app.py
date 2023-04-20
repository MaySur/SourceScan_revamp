from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Article
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)

# configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Light@0529202'
app.config['MYSQL_DB'] = 'soursescan'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# intialize mysql

mysql = MySQL(app)

Article = Article()
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def dataSource():
    return render_template('data.html', articles = Article)

@app.route('/contact')
def contact():
    return render_template('contact.html')
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():

        # mysql stuff
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data) )# encryption with sha
        # creating the cursor
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email,username,password) VALUES (%s ,%s, %s, %s)", (name, email, username, password))

        #commiting to db

        mysql.connection.commit()

        #close connection
        cur.close()

        flash(f'You are registered and log in with the username: {username}', 'success')

        return redirect(url_for('index'))


    return render_template('register.html', form=form)
if __name__ == '__main__':
    app.secret_key='secret_2468'
    app.run(debug=True)