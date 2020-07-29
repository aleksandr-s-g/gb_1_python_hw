class Worker():
    name: str
    surname: str
    position: str
    _income = {'wage': int, 'bonus': int}

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p = Position("John", "Doe", "Sales manager", 100, 10)
print(f"name {p.name}, surname {p.surname}, positinon {p.position}")
print(f"full name {p.get_full_name()}")
print(f"total income {p.get_total_income()}")

