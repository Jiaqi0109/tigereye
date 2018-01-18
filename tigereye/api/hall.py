
from flask import jsonify, request
from flask_classy import FlaskView
from tigereye.models.cinema import Cinema
from tigereye.models.hall import Hall
from tigereye.models.seat import Seat


class HallView(FlaskView):

    def seats(self):
        hid = request.args.get('hid')
        hall = Hall.get(hid)
        if not hall:
            return jsonify({'msg': 'Hall %s not found' % hid})
        hall.seats = Seat.query.filter_by(hid=hid).all()
        return jsonify(hall)
