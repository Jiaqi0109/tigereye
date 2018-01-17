from flask import Flask
from tigereye.api.misc import MiscView
from tigereye.api.cinema import CinemaView
from tigereye.api.movie import MovieView
from tigereye.models import db, JSONEncoder


def create_app(debug=True):
    app = Flask(__name__)
    app.config.from_object('tigereye.configs.default.DafalutConfig')
    app.json_encoder = JSONEncoder
    MiscView.register(app)
    CinemaView.register(app)
    MovieView.register(app)
    db.init_app(app)
    return app
