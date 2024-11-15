# TODO решите задачу
import json


def calculate_sum_of_products(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("JSON должен содержать список объектов.")

        total = 0
        for entry in data:
            if isinstance(entry, dict) and 'score' in entry and 'weight' in entry:
                total += entry['score'] * entry['weight']

        return round(total, 3)

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь.")
        return None
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON. Проверьте формат файла.")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


file_path = 'input.json'

result = calculate_sum_of_products(file_path)
if result is not None:
    print(result)
