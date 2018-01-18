from flask import jsonify, request
from flask_classy import FlaskView
from tigereye.models.cinema import Cinema
from tigereye.models.hall import Hall


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

    def halls(self):
        cid = request.args['cid']
        cinema = Cinema.get(cid)
        if not cinema:
            return jsonify({'msg': 'Cinema %s not found' % cid})
        # 查询数据库中的hall表，取出所有cid等于当前影院的影厅
        cinema.halls = Hall.query.filter_by(cid=cid).all()
        return jsonify(cinema)
