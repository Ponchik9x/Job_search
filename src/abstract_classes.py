from abc import ABC, abstractmethod

from src.interactions_with_vacancies import Vacancy


class BaseHeadHunterAPI(ABC):

    @abstractmethod
    def _connect_to_api(self):
        """Получение вакансий из HH с помощью API и сохранение в список"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, quantity: int):
        """Получение вакансий по ключевому слову"""
        pass


class BaseAddingVacancies(ABC):
    """Абстрактный класс для добавления/получения/уделения вакансий в файле"""

    @abstractmethod
    def get_data_vacancies(self):
        pass

    @abstractmethod
    def add_vacancy(self, value: list[Vacancy]):
        pass

    @abstractmethod
    def delete_vacancy(self, id_vacancy):
        pass
