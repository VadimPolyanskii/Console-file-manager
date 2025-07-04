# Программа "Консольный файловый менеджер"
# cmd + F5 - обновление проекта
import os
import shutil
from pathlib import Path


def file_manager():
    while True:
        # Меню
        # cmd + F5 - обновление проекта после каждой операции
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
        if choice == '1':    # Создать папку
            name_folder = input("Введите имя папки: ")
            os.makedirs(name_folder, exist_ok=True)         # Создаём папку
            print(f"Папка {name_folder} создана")
        elif choice == '2':    # Удаление папки
            deleted_folder = input("Введите имя папки: ")
            data_deleted_folder = os.path.join(os.getcwd(), deleted_folder)   # Формируем путь до указанной папки
            shutil.rmtree(data_deleted_folder)     # Удаляем папку
            print(f"{deleted_folder} и её содержимое удалены")
        elif choice == '3':    # Копировать папку
            copied_folder = input("Введите название папки: ")
            data_copied_folder = os.path.join(os.getcwd(), copied_folder) # Формируем путь до указанной папки
            new_folder = input("Введите имя новой папки: ")
            shutil.copytree(data_copied_folder, new_folder, dirs_exist_ok=True)  # Копия папки появится даже если уже есть такая копия
            print(f"{new_folder} создана")
        elif choice == '4':   # Просмотр рабочей директории
            print("Текущая директория:", os.getcwd())
        elif choice == '5':     # Просмотр только папок
            path = Path(os.getcwd())
            folders = [f.name for f in path.iterdir() if f.is_dir()]
            print(folders)
        elif choice == '6':     # Просмотр только файлов
            files = [file.name for file in os.scandir(os.getcwd()) if file.is_file()]
            print(f"Список всех файлов в текущей дериктории: {files}")
        elif choice == '7':     # Просмотр инф-ии об ОП
            from platform import system
            print(f"Операционная система: {system()}")
        elif choice == '8':     # Создатель программы
            print("Создатель программы: Вадим Полянский")
        elif choice == '9':     # Игра в викторину
            import victory
            print(victory.quiz())
        elif choice == '10':     # Банковский счёт
            import use_function
            print(use_function.personal_account())
        elif choice == '11':    # Смена рабочей директории
            new_directory = input("Введите путь к новой директории: ")
            os.chdir(new_directory)
            print(f"Новая текущая директория: {Path.cwd()}")
        else:
            print("Выход")
            break


file_manager()