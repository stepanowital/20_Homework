import pytest

from service.genre import GenreService


class TestGenreService:

	@pytest.fixture(autouse=True)
	def genre_service(self, genre_dao):
		self.genre_service = GenreService(dao=genre_dao)

	def test_get_all(self):
		genres = self.genre_service.get_all()

		assert genres is not None
		assert len(genres) > 0

	def test_get_one(self):
		genre = self.genre_service.get_one(1)

		assert genre is not None
		assert genre.id == 1
		assert genre.name == "HOHOHO"

	def test_create(self):
		genre_d = {}
		genre = self.genre_service.create(genre_d)

		assert genre is not None
		assert genre.id == 4
		assert genre.name == "COMEDY"

	def test_update(self):
		genre_d = {}
		genre = self.genre_service.update(genre_d)

		assert genre is not None

	def test_delete(self):
		genre = self.genre_service.delete(1)

		assert genre is None

	# def test_partially_update(self):
	# 	genre_d = {"id": 1, "name": "Baron1"}
	# 	assert self.genre_service.partially_update(genre_d)

