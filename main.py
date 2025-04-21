from src.interactions_with_API import Vacancy, HeadHunterAPI
from src.interactions_with_files import JSONSaver
from src.utils import filter_vacancies


def user_interaction():
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python", 5)
    file_handler = JSONSaver()
    file_handler.add_to_file(hh_vacancies)


    while True:
        print("\n1. Получить вакансии по запросу")
        print("2. Получить минимальную зарплату по вакансии")
        print("3. Удалить вакансию по названию")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            keyword = input('Введите ключевое слово для поиска вакансий: ')
            vacancies_data = hh_api.get_vacancies(keyword)
            vacancies = []
            for item in vacancies_data:
                vacancy = Vacancy(
                    id=item['id'],
                    name=item['name'],
                    salary=item['salary']['from'] if item['salary'] else 0,
                    url=item['alternate_url']
                )
                vacancies.append(vacancy)


            for vacancy in vacancies:
                file_handler.save_in_file([{
                'id': vacancy.id,
                'title': vacancy.name,
                'salary': vacancy.salary,
                'url': vacancy.url
            } ])
                print(f"Добавлена вакансия: {vacancy.name}")

        elif choice == '2':
            min_salary = float(input('Введите минимальную зарплату: '))
            filtered_vacancies = filter_vacancies([{
                'id': vacancy.id,
                'title': vacancy.name,
                'salary': vacancy.salary,
                'url': vacancy.url
            } for vacancy in vacancies], min_salary)
            print('Отфильтрованные вакансии: ')
            for vacancy in filtered_vacancies:
                print(vacancy)

        elif choice == '3':
            title = input("Введите название вакансии для удаления: ")
            file_handler.delete_vacancy(title)
            print(f"Вакансия '{title}' удалена.")

        elif choice == '4':
            break






if __name__ == '__main__':

    user_interaction()





