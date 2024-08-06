from flask import Flask

def create_app():
    app = Flask(__name__)

    from routes.views import views
    from routes.auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)