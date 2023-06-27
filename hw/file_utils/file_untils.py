from file_utils import json_utils, csv_utils, pickle_utils, directory_utils

# Загрузка данных из JSON файла
data = json_utils.load_json('data.json')

# Сохранение данных в CSV файл
csv_utils.save_csv('data.csv', data, fieldnames=['name', 'age', 'city'])

# Загрузка данных из pickle файла
data = pickle_utils.load_pickle('data.pickle')

# Рекурсивный обход директории и сохранение результатов
directory_utils.save_directory_contents('/path/to/directory')
