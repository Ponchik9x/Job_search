from src.interactions_with_API import HeadHunterAPI
from src.interactions_with_files import JSONSaver
from src.interactions_with_vacancies import Vacancy


def user_interaction():
    hh_api = HeadHunterAPI()
    file_handler = JSONSaver()

    while True:
        print("\n1. Получить вакансии по запросу")
        print("2. Получить минимальную зарплату по вакансии")
        print("3. Удалить вакансию по названию")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            vacancies_data = hh_api.get_vacancies(keyword)
            vacancies = []
            for item in vacancies_data:
                vacancy = Vacancy(
                    id=item["id"],
                    name=item["name"],
                    salary=item["salary"]["from"] if item["salary"] else 0,
                    url=item["alternate_url"],
                )
                vacancies.append(vacancy)

                print(f"Добавлена вакансия: {vacancy}")
            file_handler.add_vacancy(vacancies)

        elif choice == "2":
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            vacancies_data = hh_api.get_vacancies(keyword)
            min_salary = float(input("Введите минимальную зарплату: "))
            # filtered_vacancies = sorted(vacancies_data, reverse=True)
            filtered_vacancies = []
            for v in vacancies_data:
                if v["salary"] is not None:
                    if v["salary"]["from"] is not None:
                        if v["salary"]["from"] > min_salary:
                            filtered_vacancies.append(v)
                    else:
                        if v["salary"]["to"] > min_salary:
                            filtered_vacancies.append(v)
            return print(filtered_vacancies)

            #     if float(v["salary"]) > min_salary:
            #         filtered_vacancies.append(v)
            # print("Отфильтрованные вакансии: ")
            # for vacancy in filtered_vacancies:
            #     print(vacancy)

        elif choice == "3":
            title = input("Введите название вакансии для удаления: ")
            file_handler.delete_vacancy(title)
            print(f"Вакансия '{title}' удалена.")

        elif choice == "4":
            break
