from unittest.mock import MagicMock

import pytest

from dao.model.director import Director
from dao.director import DirectorDAO

from dao.model.genre import Genre
from dao.genre import GenreDAO

from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
	director_dao = DirectorDAO(None)

	d1 = Director(id=1, name="Baron")
	d2 = Director(id=2, name="Agatanov")
	d3 = Director(id=3, name="Folmer")
	d4 = Director(id=4, name="Vinnik")

	directors = {1: d1, 2: d2, 3: d3, 4: d4}

	director_dao.get_one = MagicMock(return_value=d1)
	director_dao.get_all = MagicMock(return_value=directors.values())
	director_dao.create = MagicMock(return_value=d4)
	director_dao.delete = MagicMock()
	director_dao.update = MagicMock()
	director_dao.partially_update = MagicMock(return_value=d4)

	return director_dao


@pytest.fixture()
def genre_dao():
	genre_dao = GenreDAO(None)

	g1 = Genre(id=1, name="HOHOHO")
	g2 = Genre(id=2, name="HORROR")
	g3 = Genre(id=3, name="DRAMA")
	g4 = Genre(id=4, name="COMEDY")

	genres = {1: g1, 2: g2, 3: g3, 4: g4}

	genre_dao.get_one = MagicMock(return_value=g1)
	genre_dao.get_all = MagicMock(return_value=genres.values())
	genre_dao.create = MagicMock(return_value=g4)
	genre_dao.delete = MagicMock()
	genre_dao.update = MagicMock()
	genre_dao.partially_update = MagicMock(return_value=g4)

	return genre_dao


@pytest.fixture()
def movie_dao():
	movie_dao = MovieDAO(None)

	m1 = Movie(id=1, title="Титул1", description="Описание1", trailer="Трэйлер1", year=2001, rating=1, genre_id=5,
			   director_id=5)
	m2 = Movie(id=2, title="Титул2", description="Описание2", trailer="Трэйлер2", year=2002, rating=2, genre_id=5,
			   director_id=5)
	m3 = Movie(id=3, title="Титул3", description="Описание3", trailer="Трэйлер3", year=2003, rating=3, genre_id=5,
			   director_id=5)
	m4 = Movie(id=4, title="Титул4", description="Описание4", trailer="Трэйлер4", year=2004, rating=4, genre_id=5,
			   director_id=5)

	movies = {1: m1, 2: m2, 3: m3, 4: m4}

	movie_dao.get_one = MagicMock(return_value=m1)
	movie_dao.get_all = MagicMock(return_value=movies.values())
	movie_dao.create = MagicMock(return_value=m4)
	movie_dao.delete = MagicMock()
	movie_dao.update = MagicMock()
	movie_dao.partially_update = MagicMock(return_value=m4)

	return movie_dao
