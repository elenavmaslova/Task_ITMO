import csv
from collections import Counter

def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        results = []
        # Чтение данных
        for row in reader:
            results.append(row)
        return results

def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    try:
        if not isinstance(floor_count, int):
            raise TypeError
        if floor_count <= 0:
            raise ValueError
    except TypeError:
        print("Ошибка: Введено не число!")
    except ValueError:
        print("Ошибка: Введено некорректное число!")
    else:
        if 0 < floor_count < 6:
            return "Малоэтажный"
        elif 5 < floor_count < 17:
            return "Среднеэтажный"
        elif floor_count > 16:
            return "Многоэтажный"

def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    category_house = []
    for house in houses:
        category_house.append(classify_house(int(house["floor_count"])))
    return category_house

def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    return Counter(categories)

def min_area_residential(houses: list[dict]) -> str:
    """Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.
    """
    address = ""
    min = 10000
    for house in houses:
        if (float(house["area_residential"]) / float(house["population"])) < min:
            min = float(house["area_residential"]) / float(house["population"])
            return (f" Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца. {house['house_address']}")

houses = read_file("housing_data.csv")
print(get_count_house_categories(get_classify_houses(houses)))
print(min_area_residential(houses))
