from tigereye.api import ApiView
from tigereye.helper.code import Code
from tigereye.models.movie import Movie


class MovieView(ApiView):
    def all(self):
        movies = Movie.query.all()
        return movies
