class FigureColor:
    """
    Класс «Цвет фигуры»
    """

    def __init__(self):
        self._color = None #Инициализация

    @property
    def colorproperty(self):
        """
        get-аксессор
        """
        return self._color

    @colorproperty.setter
    def colorproperty(self, value):
        """
        Setu-аксессор
        """
        self._color = value