from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("base.html")

@views.route("/profile")
def profile():
    return render_template("profile.html")

# @views.route("/test")
# def index():
#     return render_template("index.html")