class Vacancy:
    __slots__ = ('_id', '_name', '_salary', '_url')

    def __init__(self, id, name,  url: str, salary: float|int):
        self._id = id
        self._name = self.__validate_name(name)
        self._url = self.__validate_url(url)
        self._salary = self.__validate_salary(salary)

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary <= other.salary

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary != other.salary

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary >= other.salary

    def __repr__(self):
        return  f"Vacancy(id={self._id}, title={self._company}, salary={self._salary}, url={self._url}"

    @staticmethod
    def __validate_company(company):
        if not isinstance(company, str) or not company:
            return "нет названия компании работодателя."
        return company

    @staticmethod
    def __validate_name(name):
        if not isinstance(name, str) or not name:
            return "нет названия вакансии."
        return name

    @staticmethod
    def __validate_salary(salary):
        if not isinstance(salary, (int, float)) or not salary < 0:
            return 0
        return salary

    @staticmethod
    def __validate_url(url):
        if not isinstance(url, str) or not url.startswith("http"):
            return "нет ссылки"
        return url


    @property
    def id(self):
        return self._id

    @property
    def salary(self):
        return self._salary

    @property
    def url(self):
        return self._url

    @property
    def name(self):
        return self._name

    @salary.setter
    def salary(self, value: float):
        if value is None:
            self._salary = 0
        elif not isinstance(value, (int, float)) or value < 0:
            raise ValueError('Проверьте значение ввода зарплаты. Значение должно быть положительным числом.')
        else:
            self._salary = value


    # @classmethod
    # def cast_to_object_list(cls, value):
    #     print(value[0])
