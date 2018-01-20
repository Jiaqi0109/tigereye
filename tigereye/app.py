from logging import FileHandler, Formatter
import os
import logging
from logging.handlers import SMTPHandler

from flask import Flask
from flask_classy import FlaskView

from tigereye.models import JSONEncoder, db


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('tigereye.configs.default.DefalutConfig')
    app.config.from_object(config)
    app.json_encoder = JSONEncoder

    # 处理log
    if not app.debug:
        app.logger.setLevel(logging.INFO)

        mail_handler = SMTPHandler(
            app.config['EMAIL_HOST'],
            app.config['SERVER_EMAIL'],
            app.config['ADMINS'],
            'TIGEREYE ALERT',
            credentials=(app.config['EMAIL_HOST_USER'],
                         app.config['EMAIL_HOST_PASSWORD'])
        )
        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(Formatter('''
        Message Type: %(levelname)s
        Location:     %(pathname)s:  %(lineno)d
        Module:       %(module)s
        Function:     %(funcName)s
        Time:         %(asctime)s
        
        Message:
        
        %(message)s
        '''))
        app.logger.addHandler(mail_handler)

        file_handler = FileHandler(os.path.join(app.config['LOG_DIR'], 'app.log'))
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s : %(message)s'
        ))
        app.logger.addHandler(file_handler)

    configure_views(app)
    db.init_app(app)
    app.logger.info('app created succ.')
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
