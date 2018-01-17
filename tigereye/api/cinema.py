from flask import jsonify, request
from flask_classy import FlaskView
from tigereye.models.cinema import Cinema


class CinemaView(FlaskView):

    def all(self):
        cinemas = Cinema.query.all()
        print(cinemas)
        return jsonify(cinemas)

    def get(self):
        cid = request.args['cid']
        cinema = Cinema.get(cid)
        if not cinema:
            return jsonify({'msg': 'Cinema %s not found' % cid})
        return jsonify(cinema)
