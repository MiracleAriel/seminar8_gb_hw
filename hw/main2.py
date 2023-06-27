# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.

import csv
import pickle

def read_csv_as_pickle(csv_file):
    try:
        with open(csv_file, 'r', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)  # Пропуск заголовка
            data = list(reader)    # Считывание данных
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied for reading file '{csv_file}'.")
        return
    except csv.Error:
        print(f"Error: Failed to read CSV file '{csv_file}'.")
        return

    try:
        pickle_data = pickle.dumps(data)  # Преобразование данных в строку формата pickle
        return pickle_data
    except pickle.PicklingError:
        print(f"Error: Failed to pickle data from CSV file '{csv_file}'.")
        return

# Пример использования функции
csv_file = "data.csv"
pickle_data = read_csv_as_pickle(csv_file)

if pickle_data:
    print(pickle_data)
