from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return "<p>Home</p>"

@views.route("/profile")
def profile():
    return "<p>Profile</p>"