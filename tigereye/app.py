from flask import Flask
from tigereye.models import db, JSONEncoder
from flask_classy import FlaskView


def create_app(debug=True):
    app = Flask(__name__)
    app.config.from_object('tigereye.configs.default.DafalutConfig')
    app.json_encoder = JSONEncoder
    configure_views(app)
    db.init_app(app)
    return app


def configure_views(app):
    from tigereye.api.misc import MiscView
    from tigereye.api.cinema import CinemaView
    from tigereye.api.movie import MovieView
    from tigereye.api.hall import HallView

    for view in locals().values():
        if type(view) == type and issubclass(view, FlaskView):
            view.register(app)
