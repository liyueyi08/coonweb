from app1 import app
from flask import render_template
import forms
#@app.route creating different address to get to the same Flask object
#decor allow index() to be run whenever the route is accessed
@app.route("/")
@app.route("/home")
def index():
    #render template can do more than opening the file, it allow us to modify file
    return render_template("index.html", head2="My Space")

@app.route("/about")
def about():
    return render_template("about.html", about_head1="Coon's info", about_p1="She is a mysterious creature",about_head2="Surprise")

#methods argument allow the page to handle post request from user
@app.route("/noteboard", methods = ["GET", "POST"])
def note():
    f = forms.AddTaskForm()
    if f.validate_on_submit():
        return render_template("notes.html", form = f, title = f.title.data)
    return render_template("notes.html", form = f)
