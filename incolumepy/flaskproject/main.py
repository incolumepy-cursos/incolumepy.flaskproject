from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'id': 5,
        'author': 'Ada Catarina Santos Brito',
        'title': 'post 5',
        'content': 'content post 5',
        'posted': '09-07-2021 15:58',
    },
    {
        'id': 4,
        'author': 'Ana Gabriela Santos Brito',
        'title': 'post 4',
        'content': 'content post 4',
        'posted': '09-07-2021 15:58',
    },
    {
        'id': 3,
        'author': 'Eliana Ferreira dos Santos Brito',
        'title': 'post 3',
        'content': 'content post 3',
        'posted': '09-07-2021 15:53',
    },
    {
        'id': 2,
        'author': 'Ricardo Brito do Nascimento',
        'title': 'post 2',
        'content': 'content post 2',
        'posted': '09-07-2021 15:03',
    },
    {
        'id': 1,
        'author': 'Ricardo Brito do Nascimento',
        'title': 'post 1',
        'content': 'content post 1',
        'posted': '09-07-2021 15:00',
    }
]


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/')
def home():
    title = "Home Page"
    return render_template('home.html', title=title, posts=posts)
