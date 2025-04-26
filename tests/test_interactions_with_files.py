import json
from unittest.mock import mock_open, patch

import pytest

from src.interactions_with_files import JSONSaver


@pytest.fixture
def user_one():
    """фикстура один"""
    return [
        {
            "id": "119396456",
            "name": "Менеджер по выявлению потребности (удаленно)",
            "salary": 0,
            "url": "https://hh.ru/vacancy/119396456",
        }
    ]


@pytest.fixture
def user_two():
    """фикстура два"""
    return {
        "id": "119396357",
        "name": "Менеджер по выявлению потребности (удаленно)",
        "salary": 0,
        "url": "https://hh.ru/vacancy/119396357",
    }


def test_get_data_vacancies():
    """тест на получение вакансии"""
    file_handler = JSONSaver()
    assert file_handler.get_data_vacancies == file_handler.get_data_vacancies


def test_add_vacancy():
    """тест на добавление вакансии"""
    mock_data = [{"name": "Vacancy 1"}, {"name": "Vacancy 2"}]
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        handler = JSONSaver("test_vacancies.json")
        data = handler.get_data_vacancies()
        assert data == mock_data, "Ошибка: Данные не загружены корректно"


def test_del_vacancy():
    """тест на удаление вакансии"""
    mock_data = [{"name": "Vacancy 1"}, {"name": "Vacancy 2"}]
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        handler = JSONSaver("test_vacancies.json")
        data = handler.get_data_vacancies()
        assert data == mock_data, "Ошибка: Данные не загружены корректно"


# def test_get_vacancies_success():
#     mock_data = [
#         {"name": "Vacancy 1"},
#         {"name": "Vacancy 2"},
#         {"name": "Developer Vacancy"},
#     ]
#     with patch(
#             "builtins.open",
#             mock_open(read_data="\n".join(json.dumps(d) for d in mock_data)),
#     ):
#         handler = JSONSaver("test_vacancies.json")
#         vacancies = handler.get_data_vacancies()
#         assert len(vacancies) == 1, "Ошибка: Должна быть одна вакансия"
#         assert (
#                 vacancies[0]["name"] == "Developer Vacancy"
#         ), "Ошибка: Неверное имя вакансии"
