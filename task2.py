from abc import ABC, abstractmethod


class Сlothes(ABC):
    _name = ""

    def __init__(self, name : str):
        self._name = name

    @abstractmethod
    def textile(self):
        pass


class Coat(Сlothes):
    _size: int

    def __init__(self, size: int):
        self._size = size
        super().__init__("Coat")

    @property
    def textile(self):
        return self._size/6.5+0.5



class Suit(Сlothes):
    _height: int

    def __init__(self, height: int):
        self._height = height
        super().__init__("Suit")

    @property
    def textile(self):
        return self._height*2+0.3


clothes_list = [Coat(54), Suit(180)]
for c in clothes_list:
    print(round(c.textile,2))
