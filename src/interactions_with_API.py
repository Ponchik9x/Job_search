import requests

from src.abstract_classes import BaseHeadHunterAPI


class HeadHunterAPI(BaseHeadHunterAPI):

    def __init__(self):
        self.__hh_url = "https://api.hh.ru/vacancies"

    def __str__(self):
        return self.__hh_url

    def _connect_to_api(self, params=None):
        """подключение к API hh.ru"""
        response = requests.get(self.__hh_url, params=None)
        if response.status_code != 200:
            raise Exception("Ошибка подключения: 404")
        return response

    def get_vacancies(self, text: str, per_page: int = 60):
        """получение вакансий из hh.ru"""

        params = {"text": text, "per_page": per_page}
        response = self._connect_to_api(params=params)
        # response = requests.get(self.__hh_url, params=params)
        return response.json().get("items", [])
