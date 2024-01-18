import csv
import json


def convert_csv_to_json(csv_file):
    # Открываем CSV файл для чтения
    with open(csv_file, 'r') as file:
        # Создаем DictReader для чтения значений из CSV файла
        reader = csv.DictReader(file)

        # Создаем список для хранения словарей в формате JSON
        json_data = []

        # Проходимся по каждой строке в CSV файле
        for row in reader:
            # Создаем словарь для текущей строки
            data = {}

            # Проходимся по каждому столбцу в текущей строке
            for column, value in row.items():
                # Добавляем столбец и значение в словарь
                data[column] = value

            # Добавляем словарь в список
            json_data.append(data)

    # Преобразуем список словарей в строку формата JSON с отступами равными 4
    json_string = json.dumps(json_data, indent=4)

    # Возвращаем строку формата JSON
    return json_string


# Пример использования
csv_file = 'data.csv'
json_string = convert_csv_to_json(csv_file)
print(json_string)