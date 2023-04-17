from flask import Flask, render_template
from data import Article


app = Flask(__name__)
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


if __name__ == '__main__':
    app.run(debug=True)