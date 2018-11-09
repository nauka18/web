import os
from flask import Flask

""" create and configure the app """
def createApp(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(    #default configurations
        SECRET_KEY = 'dev',  # only in debug!
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    app.config.from_pyfile('config.py', silent=True)

    from . import auth, landpage
    app.register_blueprint(auth.bp)
    app.register_blueprint(landpage.bp)

    return app
