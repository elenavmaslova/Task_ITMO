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
        for res in results:
            res['floor_count'] = int(res['floor_count'])
            res['population'] = int(res['population'])
            res['heating_value'] = float(res['heating_value'])
            res['area_residential'] = float(res['area_residential'])
        return results

def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """

    if not isinstance(floor_count, int):
        print("Ошибка: Введено не число!")
    elif floor_count <= 0:
        print("Ошибка: Введено некорректное число!")
    elif 0 < floor_count < 6:
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
        category_house.append(classify_house(house["floor_count"]))
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
    min_ = float("+inf")
    for house in houses:
        if (float(house["area_residential"]) / float(house["population"])) < min_:
            min_ = float(house["area_residential"]) / float(house["population"])
            return (house['house_address'])

houses = read_file("housing_data.csv")
print(houses)
print(get_count_house_categories(get_classify_houses(houses)))
print(min_area_residential(houses))
