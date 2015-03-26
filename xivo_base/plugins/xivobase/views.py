from flask import Blueprint
from flask import render_template, redirect, url_for

xivobase = Blueprint('xivobase', __name__, template_folder='templates')

@xivobase.route("/")
def index():
    return render_template('xivobase.html')

