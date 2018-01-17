from flask import jsonify
from flask_classy import FlaskView
from tigereye.models.movie import Movie


class MovieView(FlaskView):
    def all(self):
        movies = Movie.query.all()
        print(movies)
        return jsonify(movies)
