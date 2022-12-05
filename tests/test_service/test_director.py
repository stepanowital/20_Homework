import pytest

from service.director import DirectorService


class TestDirectorService:

	@pytest.fixture(autouse=True)
	def director_service(self, director_dao):
		self.director_service = DirectorService(dao=director_dao)

	def test_get_all(self):
		directors = self.director_service.get_all()

		assert directors is not None
		assert len(directors) > 0

	def test_get_one(self):
		director = self.director_service.get_one(1)

		assert director is not None
		assert director.id == 1
		assert director.name == "Baron"

	def test_create(self):
		director_d = {}
		director = self.director_service.create(director_d)

		assert director is not None
		assert director.id == 4
		assert director.name == "Vinnik"

	def test_update(self):
		director_d = {}
		director = self.director_service.update(director_d)

		assert director is not None

	def test_delete(self):
		director = self.director_service.delete(1)

		assert director is None

	def test_partially_update(self):
		director_d = {"id": 1, "name": "ФонБарон"}

		director = self.director_service.partially_update(director_d)

		assert director is not None
		assert director.name == "ФонБарон"
