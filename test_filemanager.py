# В файле написать тесты для каждой "чистой" функции, чем больше тем лучше.
# Это могут быть функции "Консольного файлового менеджера",
# а также программы "Мой счет" и программы "Викторина"

# Библиотеки для работы с файловой системой
import os
import shutil
from pathlib import Path

import pytest               # Фреймворк для тестирования
from step_1 import *        # Импорт всех функций модуля step_1
from use_function import PersonalAccount     # Импорт класса из модуля use_function


@pytest.fixture
# Тестирование файлового менеджера
def setup_teardown():
    # Фикстура setup_teardown создаёт папку test_folder перед каждым тестом (Setup)
    # Setup
    test_folder = "test_folder"
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    yield test_folder       # передаёт имя папки в тест
    # Teardown
    # Удаляет папку после теста
    if os.path.exists(test_folder):
        shutil.rmtree(test_folder)


# Тест создания папки
def test_create_folder(setup_teardown):
    result = create_folder(setup_teardown)      # Получаем результат из тестируемой функции
    assert os.path.exists(setup_teardown)
    assert  result == f"Папка {setup_teardown} создана"


# Тест удаления папки
def test_delete_folder(setup_teardown):
    result = delete_folder(setup_teardown)      # Получаем результат из тестируемой функции
    assert not os.path.exists(setup_teardown)       # Проверяем, что папка удалена
    assert result == f"{setup_teardown} и её содержимое удалены"


# Тест копирования папки
def test_copy_folder(setup_teardown):
    new_folder = "copied_test_folder"
    result = copy_folder(setup_teardown, new_folder)        # Получаем результат из тестируемой функции
    assert os.path.exists(new_folder)       # Проверяем наличие новой (копии) папки
    assert result == f"{new_folder} создана"
    shutil.rmtree(new_folder)       # Очистка


# Тест текущей дериктории
def test_get_current_diectory(setup_teardown):
    result = get_current_directory()        # Получаем результат из тестируемой функции
    assert result == os.getcwd()            # Проверяем, что result - это текущая директория


# Тест списка папок
def test_list_folders(setup_teardown):
    result = list_folders()     # Получаем результат из тестируемой функции
    assert isinstance(result, list)         # Проверяем, что result - это список
    assert setup_teardown in result         # Проверяем, что тестовая папка есть в списке


# Тест списка файлов
def test_list_files():
    test_file = "test_file.txt"         # Создаём временный файл
    with open(test_file, 'w') as f:     # открываем его в режиме перезаписи
        f.write("test")                 # и делаем в нем запись "test"

    result = list_files()       # Получаем результат из тестируемой функции
    assert isinstance(result, list)     # Проверяем, что result - это список
    assert test_file in result          # Проверяем, что test_file есть в result

    os.remove(test_file)                # Удаляем временный файл


# Тест информации об ОС
def test_get_os_info():
    result = get_os_info()          # Получаем результат из тестируемой функции: информацию об ОС
    assert "Операционная система" in result         # Проверяет наличие ключевой фразы в результате


# Тест смены директории
def test_change_directory(setup_teardown):
    original_dir = os.getcwd()          # Запоминаем текущюю директорию
    result = change_directory(setup_teardown)       # Меняем текущую директорию на тестовую
    assert os.getcwd() == os.path.join(original_dir, setup_teardown)   # Проверяем, что текущая директория сменилась правильно
    assert f"Новая текущая директория: {os.getcwd()}" in result        # Проверяем корректность сообщения
    os.chdir(original_dir)      # Возвращаемся в исходную директорию


# Тестирование программы "Мой счёт"
# Тест пополнения счёта
def test_deposit():
    account = PersonalAccount()             # Создаём новый счёт
    account.deposit(100)                    # Пополняем на 100
    assert account.get_balance() == 100     # Проверяем, что баланс 100


# Тест покупки
def test_purchase():
    account = PersonalAccount()         # Создаём новый счёт
    account.deposit(100)                # Пополняем на 100
    account.purchase("Книга", 50)       # Покупаем книгу за 50
    assert account.get_balance() == 50              # Проверяем баланс
    assert account.get_history() == [("Книга", 50)]     # Проверяем историю покупок


# Тест недостаточного баланса
def test_insufficient_funds():
    account = PersonalAccount()      # Создаём новый счёт
    account.deposit(10)             # Пополняем на 10
    with pytest.raises(ValueError, match="Недостаточно средств"):       # Вызывается исключение (обработка ошибок)
        account.purchase("Часы", 100)       # Пытаемся купить за 100


# Тест отрицательного пополнения
def test_negativ_deposit():
    account = PersonalAccount()         # Создаём новый счёт
    with pytest.raises(ValueError, match="Сумма пополнения должна быть положительной"):      # Вызывается исключение (обработка ошибок)
        account.deposit(-10)        # Пытаемся пополнить на -10


# Тест отрицательной покупки
def test_negativ_purchase():
    account = PersonalAccount()         # Создаём новый счёт
    account.deposit(100)            # Пополняем на 100
    with pytest.raises(ValueError, match="Сумма покупки должна быть положительной"):     # Вызывается исключение (обработка ошибок)
        account.purchase("Билет в театр", -10)          # Пытаемся купить за -10