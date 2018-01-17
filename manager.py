from flask_script import Manager, Server, Shell
from tigereye.app import create_app
from tigereye.models import db

app = create_app()
manager = Manager(app)


def _make_context():
    from tigereye.models.cinema import Cinema
    from tigereye.models.hall import Hall
    from tigereye.models.movie import Movie
    locals().update(globals())
    return dict(**locals())


manager.add_command('runserver', Server('127.0.0.1', port=5000))
manager.add_command('shell', Shell(make_context=_make_context))


@manager.command
def createdb():
    db.create_all()


if __name__ == "__main__":
    manager.run()
