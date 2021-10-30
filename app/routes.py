import flask
from app import app
from app.forms import Form


@app.route('/', methods=("GET","POST"))
def index():
    form = Form()
    if form.validate_on_submit():

        ask = form.ask.data

        print("question:", ask)
    return flask.render_template("home.html", form=form)
