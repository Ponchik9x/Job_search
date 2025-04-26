from src.interactions_with_vacancies import Vacancy


def test_valid_vacancies():
    """тест на проверку создания вакансии"""
    vacancy = Vacancy("1", "one", "http/123456qwe", 123456)
    assert vacancy.id == "1"
    assert vacancy.name == "one"
    assert vacancy.url == "http/123456qwe"
    assert vacancy.salary == 0
