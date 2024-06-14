from flask import Flask

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)

    from .app import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app