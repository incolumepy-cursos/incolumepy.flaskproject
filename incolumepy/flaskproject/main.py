from flask import Flask, render_template, flash, url_for, redirect
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "FVrpmovvW7LblKlVFmfLIk4n8X7sjuUOdIwe97udBDwLrVQtWge1cpKTwm0u137JovWZKDtFQXvZtOfBE0dLAz8H7LV"

posts = [
    {
        "id": 5,
        "author": "Ada Catarina Santos Brito",
        "title": "post 5",
        "content": "content post 5",
        "posted": "09-07-2021 15:58",
    },
    {
        "id": 4,
        "author": "Ana Gabriela Santos Brito",
        "title": "post 4",
        "content": "content post 4",
        "posted": "09-07-2021 15:58",
    },
    {
        "id": 3,
        "author": "Eliana Ferreira dos Santos Brito",
        "title": "post 3",
        "content": "content post 3",
        "posted": "09-07-2021 15:53",
    },
    {
        "id": 2,
        "author": "Ricardo Brito do Nascimento",
        "title": "post 2",
        "content": "content post 2",
        "posted": "09-07-2021 15:03",
    },
    {
        "id": 1,
        "author": "Ricardo Brito do Nascimento",
        "title": "post 1",
        "content": "content post 1",
        "posted": "09-07-2021 15:00",
    },
]


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.errorhandler(404)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('error.html', error=e)


@app.route("/")
def home():
    title = "Home Page"
    return render_template("home.html", title=title, posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Conta "{form.email.data}" criada com sucesso!', "success")
        return redirect(url_for("home"))
    return render_template("register.html", form=form, title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@incolume.com.br' and form.password.data == '123':
            flash("Login with success", 'success')
            return redirect(url_for('home'))
        else:
            flash('Please check your user or password', 'danger')
    return render_template("login.html", form=form, title="Login")
