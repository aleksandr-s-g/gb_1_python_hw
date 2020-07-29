class Stationery():
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print(f"Pen class: Start drawing by {self.title}")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print(f"Pencil class: Start drawing by {self.title}")


class Handle(Stationery):
    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        print(f"Handle class: Start drawing by {self.title}")


stationeryes = [Pen(), Pencil(), Handle()]
for stationery in stationeryes:
    stationery.draw()
