import pytest
from home_work_20.demostration_solution.service.director import DirectorService

class TestDirectorService:
    """Пишем класс с тестами для DirectorService"""
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": "John"
        }
        director = self.director_service.create(director_d)
        assert director.id is not None


    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "name": "Ivan"
        }
        director = self.director_service.update(director_d)

        assert director is not None
        assert director.name is not None

