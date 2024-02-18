class Shape:
    """
    Документация на класс.
    Класс описывает фигуры
    """
    def __init__(self, color: str = "white"):
        """
        Инициализация экземпляра класса
        :param color: Цвет
        """
        self.color = color

    def __str__(self) -> str:
        return f"Shape (color: {self.color})"

    def __repr__(self) -> str:
        return f"Shape(color='{self.color}')"


class Rectangle(Shape):
    """
    Класс 'Rectangle' наследуется от класса  'Shape', расширяет его атрибутами
    'width' и 'height' и реализует метод 'calculate_area'
      """
    def __init__(self, color: str = "white", width: float = 0, height: float = 0):
        """
            Инициализация экземпляра класса
            :param width: Ширина
            :param  height:  Высота
            """
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        """
       Вычисляет площадь прямоугольника.
        Returns:
            float: Площади прямоугольника
        """
        return self.width * self.height

    def __str__(self) -> str:
        """
        Метод __str__ перегружен для печати информации о прямоугольнике
         """
        return f"Rectangle (color: {self.color}, width: {self.width}, height: {self.height})"


    def __repr__(self) -> str:
        return f"Rectangle(color='{self.color}', width={self.width}, height={self.height})"