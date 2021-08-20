from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel, Domain
from flask_user import UserManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


# Initialize Flask-BabelEx
babel = Babel()

# Use the browser's language preferences to select an available translation
@babel.localeselector
def get_locale():
    print "in locale"
    return 'fr'
#    translations = [str(translation) for translation in babel.list_translations()]
#    return request.accept_languages.best_match(translations)

def create_app():
    app = Flask(__name__, static_folder='statics')

    # TODO move to unversionned configuration file
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['USER_APP_NAME'] = "Cash Register"
    app.config['USER_ENABLE_EMAIL'] = False
    app.config['USER_ENABLE_USERNAME'] = True
    app.config['USER_ENABLE_CONFIRM_EMAIL'] = False
    app.config['USER_SHOW_USERNAME_DOES_NOT_EXIST'] = True
    app.config['BABEL_DEFAULT_LOCALE'] = 'fr'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'
    app.config['LANGUAGES'] = { 'fr', 'fr-FR', 'fr_FR' }

    print app.config


    db.init_app(app)
    babel.init_app(app)

    from .models.user import User
    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, User)

    # blueprint for auth routes of app
    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for cash register parts of app
    from .routes.register import register as regist_blueprint
    app.register_blueprint(regist_blueprint)

    return app
