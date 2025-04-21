import requests

from src.abstract_classes import BaseHeadHunterAPI
from src.interactions_with_vacancies import Vacancy


class HeadHunterAPI(BaseHeadHunterAPI):

    def __init__(self):
        self.__hh_url = "https://api.hh.ru/vacancies"


    def _connect_to_api(self, params=None):
        response = requests.get(self.__hh_url, params=None)
        if response.status_code != 200:
            raise Exception("Ошибка подключения: 404")
        return response

    def get_vacancies(self, keyword: str, per_page: int = 20):

        params = {"text": keyword, "per_page": per_page}
        response = self._connect_to_api(params=params)
        # response = requests.get(self.__hh_url, params=params)
        if response.status_code != 200:
            raise Exception("Failed to fetch vacancies")
        return response.json().get("items", [])



    # def get_vacancies(self, keyword):
    #     # vacancies = self._connect_to_api(keyword).json()["items"]
    #     # self.__vacancies.extend(vacancies)
    #     # return vacancies, print("ok")


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python")

    # vacancies1 = Vacancy(hh_vacancies)
    # vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
    #                   "Требования: опыт работы от 3 лет...")
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
# ____________________________________________________________________


# class HH(BaseHeadHunterAPI):
#     """
#     Класс для работы с API HeadHunter
#     Класс Parser является родительским классом, который вам необходимо реализовать
#     """
#
#     def __init__(self, file_worker):
#         self.url = "https://api.hh.ru/vacancies"
#         self.headers = {"User-Agent": "HH-User-Agent"}
#         self.params = {"text": "", "page": 0, "per_page": 100}
#         self.vacancies = []
#         super().__init__(file_worker)
#
#     def load_vacancies(self, keyword):
#         self.params["text"] = keyword
#         while self.params.get("page") != 20:
#             response = requests.get(self.url, headers=self.headers, params=self.params)
#             vacancies = response.json()["items"]
#             self.vacancies.extend(vacancies)
#             self.params["page"] += 1
#
#
# class AddVacancies(BaseAddingVacancies):
#
#     def __init__(self):
#         pass
#
#     def add_to_file(self):
#         pass
#
#     def get_from_file(self):
#         pass
#
#     def dell_vacancies(self):
#         pass
#
#
# class JobComparison:
#     name: str
#     link_vacancy: str
#     salary: int | float
#     requirements: str
#
#     def __init__(self, name, link_vacancy, salary, requirements):
#         self.name = name
#         self.link_vacancy = link_vacancy
#         self.salary = salary
#         self.requirements = requirements
#
#     def job_comparisons(self):
#         pass
#
#     def data_validation(self):
#         pass
