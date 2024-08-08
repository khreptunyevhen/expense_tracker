from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-in", methods=["GET", "POST"])
def sign_in():

    if request.method == "POST":
        user_name = request.form.get("name")
        user_email = request.form.get("email")
        user_password = request.form.get("password")
        user_confirm_password = request.form.get("confirm_password")

        if len(user_name) < 2:
            flash("Name should be more than 1 char", category="error")
        elif len(user_email) < 4:
            flash("Email should be more than 3 char", category="error")
        elif len(user_password) < 7:
            flash("Password should be more than 6 char", category="error")
        elif len(user_password) != len(user_confirm_password):
            flash("Passwords should be equal", category="error")
        else:
            flash("The account has been created!", category="success")

    return render_template("sign_up.html")

