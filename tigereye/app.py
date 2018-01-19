from flask import Flask
from flask_classy import FlaskView

from tigereye.models import JSONEncoder, db


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('tigereye.configs.default.DafalutConfig')
    app.config.from_object(config)
    app.json_encoder = JSONEncoder
    configure_views(app)
    db.init_app(app)
    return app


def configure_views(app):
    from tigereye.api.misc import MiscView
    from tigereye.api.cinema import CinemaView
    from tigereye.api.movie import MovieView
    from tigereye.api.hall import HallView
    from tigereye.api.play import PlayView
    from tigereye.api.seat import SeatView
    from tigereye.api.order import OrderView

    for view in locals().values():
        if type(view) == type and issubclass(view, FlaskView):
            view.register(app)
