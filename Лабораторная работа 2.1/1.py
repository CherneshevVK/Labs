import doctest


class Box:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем коробки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем коробки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество вещей должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество вещей не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_box(self) -> bool:
        ...

    def add_item_to_box(self, item: float) -> None:
        if not isinstance(item, (int, float)):
            raise TypeError("Добавляемые вещи должны быть типа int или float")
        if item < 0:
            raise ValueError("Добавляемые вещи должны положительным числом")
        ...
    def remove_item_from_box(self, estimate_item: float) -> None:
        ...

class Nest:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем гнезда должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем гнезда должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int)):
            raise TypeError("Количество птиц должно быть int")
        if occupied_volume < 0:
            raise ValueError("Количество птиц не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_nest(self) -> bool:
        ...

    def add_bird_to_nest(self, bird: float) -> None:
        if not isinstance(bird, (int)):
            raise TypeError("Добавляемые птицы должны быть типа int")
        if bird < 0:
            raise ValueError("Добавляемые птицы должны положительным числом")
        ...

    def remove_bird_from_nest(self, estimate_bird: float) -> None:
        ...
class School:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем школы должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем школы должен быть положительным числом")
        self.capacity_volume = capacity_volume
        if not isinstance(occupied_volume, (int)):
            raise TypeError("Количество школьников должно быть int")
        if occupied_volume < 0:
            raise ValueError("Количество школьников не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_school(self) -> bool:
        ...
    def add_schoolboy_to_school(self, item: float) -> None:
        if not isinstance(item, (int, float)):
            raise TypeError("Добавляемые школьники должны быть типа int ")
        if item < 0:
            raise ValueError("Добавляемые школьники должны положительным числом")
        ...

    def remove_schoolboy_from_school(self, estimate_schoolboy: float) -> None:

        ...
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
