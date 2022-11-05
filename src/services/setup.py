from datetime import timedelta
import os
from dotenv import load_dotenv

from flask_cors import CORS
from services.app import app, jwt
from services.database.session import db
from services.resources.security import authenticate, identity
from routes.beneficiary.blueprint import beneficiary_bp
from routes.employee.blueprint import employee_bp
from routes.nationality.blueprint import nationality_bp


def get_db_uri() -> str:
    user = os.environ.get("DB_USER")
    pwd = os.environ.get("DB_PASS")
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT")
    name = os.environ.get("DB_NAME")
    driver = os.environ.get("DB_DRIVER")

    return f"mssql+pyodbc://{user}:{pwd}@{host}:{port}/{name}?driver={driver}"


def setup_app_config():
    app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
    app.config["JWT_AUTH_URL_RULE"] = "/api/auth"
    app.config["JWT_EXPIRATION_DELTA"] = timedelta(
        seconds=int(os.environ.get("APP_JWT_DELTA", "300"))
    )
    app.secret_key = os.environ.get("APP_SECRET_KEY")


def register_api_routes():
    app.register_blueprint(beneficiary_bp, url_prefix="/api")
    app.register_blueprint(employee_bp, url_prefix="/api")
    app.register_blueprint(nationality_bp, url_prefix="/api")


def create_db_connection():
    db.init_app(app)


def setup_cors():
    CORS(app)


def setup_jwt():
    jwt.authentication_handler(authenticate)
    jwt.identity_handler(identity)
    jwt.init_app(app)


def setup_app():
    load_dotenv()
    setup_app_config()
    register_api_routes()
    create_db_connection()
    setup_cors()
    setup_jwt()


def start_app():
    setup_app()

    app.run(
        debug=os.environ.get("APP_DEBUG", "false").lower() == "true",
        host=os.environ.get("APP_HOST", "0.0.0.0"),
        port=os.environ.get("APP_PORT", "8080"),
    )
