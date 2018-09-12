from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

app.secret_key = os.environ["FLASK_SECRET_KEY"]

# Routes


@app.route("/")
def show_homepage():
    """
    Renders the homepage for the website
    :return: Homepage
    """
    return render_template("homepage.html")

@app.route("/resume")
def show_resume():
    """

    :return:
    """
    return render_template("resume.html")

# Running the Server

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
