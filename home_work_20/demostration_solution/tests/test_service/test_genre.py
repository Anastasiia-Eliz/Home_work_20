import pytest
from home_work_20.demostration_solution.service.genre import GenreService


class TestGenreService:
    """Пишем класс с тестами для GenreService"""
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "name": "romantic",
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id is not None


    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {
            "name": "drama"
        }
        genre = self.genre_service.update(genre_d)

        assert genre is not None
        assert genre.name is not None

