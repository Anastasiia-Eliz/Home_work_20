import pytest
from unittest.mock import MagicMock
from home_work_20.demostration_solution.dao.director import DirectorDAO
from home_work_20.demostration_solution.dao.model.director import Director
from home_work_20.demostration_solution.dao.genre import GenreDAO
from home_work_20.demostration_solution.dao.model.genre import Genre
from home_work_20.demostration_solution.dao.movie import MovieDAO
from home_work_20.demostration_solution.dao.model.movie import Movie


@pytest.fixture()
def director_dao():
	"""Создаем фикстуру с моком для DirectorDAO."""
	director_dao = DirectorDAO(None)

	jonh = Director(id=1, name='jonh')
	kate = Director(id=2, name='kate')
	max = Director(id=3, name='max')

	director_dao.get_one = MagicMock(return_value=jonh)
	director_dao.get_all = MagicMock(return_value=[jonh, kate, max])
	director_dao.create = MagicMock(return_value=Director(id=3))
	director_dao.delete = MagicMock()
	director_dao.update = MagicMock()
	return director_dao


@pytest.fixture()
def genre_dao():
	"""Создаем фикстуру с моком для GenreDAO"""
	genre_dao = GenreDAO(None)

	drama = Genre(id=1, name='drama')
	comedy = Genre(id=2, name='comedy')
	fantasy = Genre(id=3, name='fantasy')

	genre_dao.get_one = MagicMock(return_value=drama)
	genre_dao.get_all = MagicMock(return_value=[drama, comedy, fantasy])
	genre_dao.create = MagicMock(return_value=Genre(id=3))
	genre_dao.delete = MagicMock()
	genre_dao.update = MagicMock()
	return genre_dao


@pytest.fixture()
def movie_dao():
	""" Создаем фикстуру с моком для  MovieDAO"""
	movie_dao = MovieDAO(None)

	m1 = Movie(id=1, title="1+1", description="very good film", trailer="video", year=2016, rating=7.7, genre_id=1,
	           director_id=2)
	m2 = Movie(id=2, title="Titanic", description="very sad film", trailer="beautiful video", year=1997, rating=10.0,
	           genre_id=2, director_id=1)
	m3 = Movie(id=3, title="Legend", description="very interesting film", trailer="video", year=2015, rating=8.1,
	           genre_id=1, director_id=1)

	movie_dao.get_one = MagicMock(return_value=m1)
	movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
	movie_dao.create = MagicMock(return_value=Movie(id=3))
	movie_dao.delete = MagicMock()
	movie_dao.update = MagicMock()
	return movie_dao
