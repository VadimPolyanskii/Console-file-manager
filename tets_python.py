# Условие задачи (п. 2 ДЗ 6): В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки\
# math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
import pytest                   # Библиотека для тестов
import functions_for_tests      # Модуль с функциями для тестов


# filter
def test_filter_even_numbers():
    # Тест с обычным списком чисел
    assert functions_for_tests.filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    # Тест с пустым списком
    assert functions_for_tests.filter_even_numbers([]) == []

    # Тест, где нет чётных чисел
    assert functions_for_tests.filter_even_numbers([1, 3, 5]) == []

    # Тест с отрицательными числами
    assert functions_for_tests.filter_even_numbers([-2, -1, 0, 1, 2]) == [-2, 0, 2]


def test_filter_even_numbers_with_non_integers():
    # Тест с числами с плавающей точкой
    assert functions_for_tests.filter_even_numbers([1.0, -2.5, 4.0]) == [4.0]


def test_filter_even_numbers_with_strings_raises_error():
    # Проверка, что функция вызывает исключение при неверном вводе
    with pytest.raises(TypeError):
        functions_for_tests.filter_even_numbers(["1", "2", "3"])


# map
def test_map_for_number():
    # Тест возведения в квадрат списка чисел
    assert functions_for_tests.map_for_number([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]

def test_map_for_strings():
    # Тест преобразования строк в целые числа
    assert functions_for_tests.map_for_strings(["1", "2", "3"]) == [1, 2, 3]


def test_map_for_strings_upper():
    # Тест возведения строк к верхнему регистру
    assert functions_for_tests.map_for_strings_upper(["возведение", "строк", "к верхнему", "регистру"]) == ["ВОЗВЕДЕНИЕ", \
                                                                                "СТРОК", "К ВЕРХНЕМУ", "РЕГИСТРУ"]


# sorted
def test_sorted_list_number():
    # Тест сортировки чисел
    assert functions_for_tests.sorted_list_number([3, 2, 1]) == [1, 2, 3]


def test_sorted_list_number_revers():
    # Тест сортировки в обратном порядке
    assert functions_for_tests.sorted_list_number_revers([4, 1, 9, 2, 7]) == [9, 7, 4, 2, 1]


def test_sorted_string():
    """Тест сортировки строки"""
    assert functions_for_tests.sorted_string("mamba") == ["aabmm"]


def test_sorted_by_key():
    """Тест сортировки по длине слов"""
    assert functions_for_tests.sorted_by_key(["banana", "apple", "orange", "pie"]) == ["pie", "apple", "banana", "orange"]


def test_sort_students():
    # Тест сортировки по возрасту
    assert functions_for_tests.sort_students([{'name': 'Alex', 'age': 22},
                                              {'name': 'Alice', 'age': 19},
                                              {'name': 'Mat','age': 20},
                                              {'name': 'Kate', 'age': 18}]) == [{'name': 'Kate', 'age': 18},
                                                                                {'name': 'Alice', 'age': 19},
                                                                                {'name': 'Mat','age': 20},
                                                                                {'name': 'Alex', 'age': 22}]

def test_sort_tuples():
    # Тест сортировки кортежей по второму элементу
    assert functions_for_tests.sort_tuples([(1, 'c'),
                                            (3, 'a'),
                                            (2, 'b'),
                                            (4, 'd')]) == [(3, 'a'),
                                                           (2, 'b'),
                                                           (1, 'c'),
                                                           (4, 'd')]

def test_sort_with_multiple_keys():
    # Тест сортировка по первому числу, затем по второму
    assert functions_for_tests.sort_with_multiple_keys([('apple', 3, 2),
                                                        ('orange', 1, 4),
                                                        ('pear', 2, 4),
                                                        ('banana', 3, 1)]) == [('orange', 1, 4),
                                                                               ('pear', 2, 4),
                                                                               ('banana', 3, 1),
                                                                               ('apple', 3, 2)]


# Тесты над функциями из библиотеки Math
# Pi
def test_area_of_a_circle():
    # Тест на вычисление площади круга
    assert functions_for_tests.area_of_a_circle(5) == '78.54'


def test_circumference():
    # Тест на вычисление длины окружности
    assert functions_for_tests.circumference(8) == '50.27'


def test_volume_of_a_sphere():
    # Тест на вычисление объёма сферы
    assert functions_for_tests.volume_of_a_sphere(15) == '14137.17'


# sqrt
def test_square_root_calculation():
    # Тест вычисления квадратного корня из заданного числа
    assert functions_for_tests.square_root_calculation(16) == 4.0


def test_calculating_square_root_of_a_fractional_number():
    # Тест обработки ошибки при вычисления квадратного корня из отрицательного числа
    assert functions_for_tests.calculating_square_root_of_a_fractional_number(-1) == (None, 'math domain error')


def test_calculating_the_square_root_of_a_fractional_number():
    # Тест вычисления квадратного корня из дробного числа
    assert functions_for_tests.calculating_the_square_root_of_a_fractional_number(2.25) == 1.5


# pow
def test_raising_to_a_power():
    # Тест возведения в степень
    assert functions_for_tests.raising_to_a_power(2, 3) == 8.0


# hypot
def test_calculating_hypotenuse():
    # Тест вычисления гмпотенузы
    assert functions_for_tests.calculating_hypotenuse(3, 4) == 5.0