import json

from src.abstract_classes import BaseAddingVacancies


class JSONSaver(BaseAddingVacancies):

    def __init__(self, filename="data/vacancies.json"):
        self.__filename = filename



    def add_vacancy(self):
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_in_file(self, value):
        filtered_vacancies = []
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip():  # Проверяем, что строка не пустая
                        data = json.loads(line)
                        if value.lower() in data.get("name", "").lower():
                            filtered_vacancies.append(data)
        except FileNotFoundError:
            print(f"Файл {self.__filename} не найден.")
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")

        return filtered_vacancies

    def delete_vacancy(self, id_vacancy):
        vacancies = self.get_from_file()
        vacancies = [vacancy for vacancy in vacancies if vacancy.get('id') != id_vacancy]
        with open(self.__filename, 'w') as f:
            json.dumps(vacancies, f, indent=4)

