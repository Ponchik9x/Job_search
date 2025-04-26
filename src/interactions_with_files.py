import json

from src.abstract_classes import BaseAddingVacancies
from src.interactions_with_vacancies import Vacancy


class JSONSaver(BaseAddingVacancies):
    """Класс сохранения данных в файл.json"""

    def __init__(self, filename: str = "data/vacancies.json"):
        self.__filename = filename

    def __str__(self):
        return self.__filename

    def get_data_vacancies(self):
        """Получение вакансии из .json файла"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

    def add_vacancy(self, value: list[Vacancy]):
        """Добавление вакансий в файл .json"""
        try:
            with open(self.__filename, "r") as f:
                vacancies_data = json.load(f)

        except json.JSONDecodeError:
            vacancies_data = []

        for vacancy in value:

            if vacancy in vacancies_data:
                continue

            else:
                vacancies_data.append(vacancy.to_dict())

        with open(self.__filename, "w") as f:
            json.dump(vacancies_data, f, indent=4, ensure_ascii=False)

    def delete_vacancy(self, id_vacancy):
        """Удаление вакансии из списка в файле .json"""
        try:
            with open("data/vacancies.json", "r") as f:
                vacancies_data = json.load(f)

        except json.JSONDecodeError:
            vacancies_data = []

        count_vacancies = 0
        for v in vacancies_data:

            if v["id"] == id_vacancy:
                del vacancies_data[count_vacancies]
                count_vacancies += 1

            else:
                count_vacancies += 1

        with open(self.__filename, "w") as f:
            json.dump(vacancies_data, f, indent=4, ensure_ascii=False)
