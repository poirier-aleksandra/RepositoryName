# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    try:
        with open(INPUT_FILENAME, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            data = [row for row in reader]

        with open(OUTPUT_FILENAME, mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        print(f"Файл {INPUT_FILENAME} не найден. Проверьте путь.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILENAME, mode="r", encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
