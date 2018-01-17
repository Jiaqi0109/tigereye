from tigereye.models import db, Model


class Cinema(db.Model, Model):
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    address = db.Column(db.String(256), nullable=False)
    halls = db.Column(db.Integer, default=0, nullable=False)
    handle_fee = db.Column(db.Integer, default=0, nullable=False)
    buy_limit = db.Column(db.Integer, default=0, nullable=False)
    status = db.Column(db.Integer, nullable=False, index=True)
