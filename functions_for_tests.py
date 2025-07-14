# Условие задачи (п. 2 ДЗ 6): В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки\
# math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше

from math import pi, sqrt, pow, hypot


# В функциях определяем сценарий фильтрации для встроенных функций для последующего тестирования
# filter
def filter_even_numbers(numbers):
    """Фильтрует список чисел, оставляя только чётные"""
    return list(filter(lambda x: x % 2 == 0, numbers))


# map
def map_for_number(number):
    """Возводит в квадрат числа"""
    squared = map(lambda x: x**2, number)
    return list(squared)


def map_for_strings(str):
    """Преобразует строки в целые числа"""
    integers = map(int, str)
    return list(integers)


def map_for_strings_upper(str):
    """Приводит строки к верхнему регистру"""
    def to_upper(s):
        return s.upper()
    new_string = map(to_upper, str)
    return list(new_string)


# sorted
def sorted_list_number(lst):
    """Сортирует список чисел"""
    new_lst = sorted(lst)
    return new_lst


def sorted_list_number_revers(lst):
    """Сортирует список чисел в обратном порядке"""
    new_lst = sorted(lst, reverse=True)
    return new_lst


def sorted_string(text):
    """Сортирует строку"""
    sort_text = sorted(text)
    return ''.join(sort_text)


def sorted_by_key(words):
    """Сортировка по ключу"""
    sorted_words = sorted(words, key=len)    # Сортировка по длине слов
    return sorted_words


def sort_students(students):
    """
    Сортирует студентов по возрасту
    На вход принимает список словарей, где ключи имя и возраст
    """
    sorted_students = sorted(students, key=lambda x: x["age"])
    return sorted_students


def sort_tuples(tuples):
    """Сортровка кортежей"""
    sorted_tuples = sorted(tuples, key=lambda x: x[1])      # сортировка по второму элементу
    return sorted_tuples


def sort_with_multiple_keys(data):
    """
    Сортировка с несколькими ключами
    На вход подается список с кортежами, в которы по три элемента
    """
    sorted_data = sorted(data, key=lambda x: (x[1], x[2]))      # Сортировка по первому числу, а затем по второму
    return sorted_data


# Функции из math
# pi
def area_of_a_circle(r):
    """
    Вычисление площади круга
    На вход приходит радиус
    S = pi*r**2
    pi = 3.141592653589793
    """
    s = pi * r**2               # 78.54
    return f'{s:.2f}'           # округляем до двух значений после точки; вернёт строку '78.54'


def circumference(r):
    """
    Вычисление длины окружности
    С = 2pi*r
    pi = 3.141592653589793
    На вход подаётся радиус
    """
    c = 2 * pi * r
    return f'{c:.2f}'       # округляем до двух значений после точки; вернёт строку '50.27'


def volume_of_a_sphere(r):
    """
    Вычисление объёма сферы
    v = 4/3*pi*r**3
    pi = 3.141592653589793
    :param r: радиус: 15
    :return: вернёт строку '14137.17'
    """
    v = 4 / 3 * pi * r ** 3
    return f'{v:.2f}'       # округляем до двух знаков после точки


# sqrt
def square_root_calculation(x):
    """
    Вычисляет квадратный корень из заданного числа
    :param x: число
    :return: квадратный корень 4.0 из числа 16 (всегда возвращает вещественное число)
    """
    result_sqrt = sqrt(x)
    return result_sqrt


def calculating_square_root_of_a_fractional_number(number):
    """
    Вычисляет квадратный корень из заданного числа
    В случае ошибки (например, корень из отрицательного числа) возвращает None
    :param number: (int | float): Число, из которого извлекается корень
    :return: float | None: Результат вычисления или None в случае ошибки
    """
    try:
        return sqrt(number), None
    except ValueError as e:
        return None, str(e)


def calculating_the_square_root_of_a_fractional_number(number):
    """
    Вычисляет квадратный корень из заданного дробного числа
    :param number: вещественное число
    :return: квадратный корень
    """
    result = sqrt(number)
    return result


# pow
def raising_to_a_power(a, b):
    """
    Возведение в степень заданного числа
    :param number: результат
    """
    с = pow(a, b)
    return с


# hypot
def calculating_hypotenuse(a, b):
    """
    Вычисление гипотенузы прямоугольного треугольника
    :param a: число: катет 1
    :param b: число: катет 2
    :return: число: гипотенуза
    """
    result = hypot(a, b)
    return result


def working_with_coordinates(dx, dy):
    """
    Работа с координатами: вычисление расстояния между точками
    :param dx: точка а
    :param dy: точка b
    :return: расстояние между a и b
    """
    distance = hypot(dx, dy)
    return distance


def vector_norm(vector):
    """
    Векторная норма
    :param vector: Евклидова норма вектора (3, 4, 12)
    :return: 13.0
    """
    norm = hypot(hypot(vector[0], vector[1], vector[2]))
    return norm


if __name__ == "__main__":
    print(calculating_square_root_of_a_fractional_number(-1))

