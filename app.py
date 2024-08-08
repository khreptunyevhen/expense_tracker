from flask import Flask

def create_app():
    app = Flask(__name__)

    app.secret_key = b'_5#y2L"F4Q8z'

    from routes.views import views
    from routes.auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)