# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестированию возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle

def pickle_to_csv(pickle_file, csv_file):
    try:
        with open(pickle_file, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        print(f"Error: File '{pickle_file}' not found.")
        return
    except pickle.UnpicklingError:
        print(f"Error: Failed to unpickle file '{pickle_file}'.")
        return

    if not data or not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        print(f"Error: Invalid data format in file '{pickle_file}'.")
        return

    keys = set().union(*data)  # Получение уникальных ключей из всех словарей

    try:
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    except PermissionError:
        print(f"Error: Permission denied for writing file '{csv_file}'.")
        return
    except csv.Error:
        print(f"Error: Failed to write CSV file '{csv_file}'.")
        return

    print(f"CSV file '{csv_file}' successfully created from pickle file '{pickle_file}'.")

# Пример использования функции
pickle_file = "data.pickle"
csv_file = "data.csv"
pickle_to_csv(pickle_file, csv_file)
