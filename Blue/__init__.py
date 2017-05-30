from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hard to guess'  #other KeyError: 'A secret key is required to use CSRF.'(for wtf-form)
    bootstrap.init_app(app)
    from Blue.api.routes import mod
    from Blue.site.oneforsite import mod

    app.register_blueprint(site.oneforsite.mod)
    app.register_blueprint(api.routes.mod, url_prefix='/api')

    return  app