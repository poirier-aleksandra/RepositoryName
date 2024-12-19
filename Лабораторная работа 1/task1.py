import doctest


class Table:
    def __init__(self, material: str, legs: int):
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not isinstance(legs, int):
            raise TypeError("Количество ножек должно быть целым числом")
        if legs < 1:
            raise ValueError("Количество ножек должно быть не меньше 1")
        self.material = material
        self.legs = legs

    def fold(self) -> None:
        pass

    def move(self, new_location: str) -> None:
        pass


class Chair:
    def __init__(self, material: str, has_armrests: bool, adjustable_height: bool):
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not isinstance(has_armrests, bool):
            raise TypeError("Наличие подлокотников должно быть булевым значением")
        if not isinstance(adjustable_height, bool):
            raise TypeError("Регулируемость высоты должна быть булевым значением")
        self.material = material
        self.has_armrests = has_armrests
        self.adjustable_height = adjustable_height

    def sit(self) -> None:
        pass

    def adjust_height(self, height: float) -> None:
        if not self.adjustable_height:
            raise ValueError("Этот стул не поддерживает регулировку высоты.")
        if height <= 0:
            raise ValueError("Высота должна быть больше 0.")
        pass


class Bed:
    def __init__(self, size: str, has_storage: bool):
        if not isinstance(size, str):
            raise TypeError("Размер кровати должен быть строкой")
        if size not in {"одноместная", "двуспальная", "king-size"}:
            raise ValueError("Некорректный размер кровати")
        if not isinstance(has_storage, bool):
            raise TypeError("Наличие ящика для хранения должно быть булевым значением")
        self.size = size
        self.has_storage = has_storage

    def sleep(self) -> None:
        pass

    def change_bedding(self, bedding_size: str) -> None:
        if bedding_size != self.size:
            raise ValueError(
                f"Размер постельного белья '{bedding_size}' не соответствует размеру кровати '{self.size}'."
            )
        pass


if __name__ == "__main__":
    doctest.testmod()
