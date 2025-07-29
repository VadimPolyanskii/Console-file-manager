# Программа "Консольный файловый менеджер"
# cmd + F5 - обновление проекта
# file_manager.py
import os
import shutil
from pathlib import Path


def create_folder(name_folder):
    os.makedirs(name_folder, exist_ok=True)
    return f"Папка {name_folder} создана"


def delete_folder(deleted_folder):
    data_deleted_folder = os.path.join(os.getcwd(), deleted_folder)
    shutil.rmtree(data_deleted_folder)
    return f"{deleted_folder} и её содержимое удалены"


def copy_folder(copied_folder, new_folder):
    data_copied_folder = os.path.join(os.getcwd(), copied_folder)
    shutil.copytree(data_copied_folder, new_folder, dirs_exist_ok=True)
    return f"{new_folder} создана"


def get_current_directory():
    return os.getcwd()


def list_folders():
    path = Path(os.getcwd())
    return [f.name for f in path.iterdir() if f.is_dir()]


def list_files():
    return [file.name for file in os.scandir(os.getcwd()) if file.is_file()]


def get_os_info():
    from platform import system
    return f"Операционная система: {system()}"


def change_directory(new_directory):
    os.chdir(new_directory)
    return f"Новая текущая директория: {Path.cwd()}"


def file_manager():
    while True:
        print('-' * 25)
        print("1. Создать папку")
        print("2. Удалить папку")
        print("3. Копировать папку")
        print("4. Просмотр рабочей директории")
        print("5. Просмотр папок")
        print("6. Просмотр файлов")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счёт")
        print("11. Смена рабочей директории")
        print("12. Выход")
        print("–" * 25)

        choice = input("Выберите номер пункта меню: ")

        if not choice.isdigit():
            print("Пожалуйста, введите число от 1 до 12")
            continue

        choice = int(choice)

        if choice == 1:
            name_folder = input("Введите имя папки: ")
            print(create_folder(name_folder))
        elif choice == 2:
            deleted_folder = input("Введите имя папки: ")
            print(delete_folder(deleted_folder))
        elif choice == 3:
            copied_folder = input("Введите название папки: ")
            new_folder = input("Введите имя новой папки: ")
            print(copy_folder(copied_folder, new_folder))
        elif choice == 4:
            print("Текущая директория:", get_current_directory())
        elif choice == 5:
            print("Список папок:", list_folders())
        elif choice == 6:
            print("Список файлов:", list_files())
        elif choice == 7:
            print(get_os_info())
        elif choice == 8:
            print("Создатель программы: Вадим Полянский")
        elif choice == 9:
            import victory
            print(victory.quiz())
        elif choice == 10:
            import use_function
            print(use_function.personal_account())
        elif choice == 11:
            new_directory = input("Введите путь к новой директории: ")
            print(change_directory(new_directory))
        elif choice == 12:
            print("Выход")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 12")


if __name__ == "__main__":
    file_manager()


