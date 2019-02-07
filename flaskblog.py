from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'aed1142ca47c9f48563721311cea0928'
post = [
    {
        'author': 'Will Chen',
        'title': 'First',
        'content': 'First post!',
        'date': '1/27/19'
    },
    {
        'author': 'Billy Chen',
        'title': 'Second',
        'content': 'Second post!',
        'date': '1/28/19'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=post)

@app.route("/about")
def about():
    return render_template("about.html", title='About', posts=post)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.user.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "chenwill98@gmail.com" and form.password.data == "abc123":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect email or password', 'danger')
    return render_template("login.html", title='Login', form=form)

if __name__ == '__main__':
    app.run(debug = True)
