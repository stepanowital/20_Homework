import pytest

from service.movie import MovieService


class TestMovieService:

	@pytest.fixture(autouse=True)
	def movie_service(self, movie_dao):
		self.movie_service = MovieService(dao=movie_dao)

	def test_get_all(self):
		movies = self.movie_service.get_all()

		assert movies is not None
		assert len(movies) > 0

	def test_get_one(self):
		movie = self.movie_service.get_one(1)

		assert movie is not None
		assert movie.id == 1
		assert movie.title == "Титул1"

	def test_create(self):
		movie_d = {}
		movie = self.movie_service.create(movie_d)

		assert movie is not None
		assert movie.id == 4
		assert movie.description == "Описание4"

	def test_update(self):
		movie_d = {}
		movie = self.movie_service.update(movie_d)

		assert movie is not None

	def test_delete(self):
		movie = self.movie_service.delete(1)

		assert movie is None

	# def test_partially_update(self):
	# 	movie_d = {"id": 1, "name": "Baron1"}
	# 	assert self.movie_service.partially_update(movie_d)

