from calendar import monthrange


class Data:
    day: int
    month: int
    year: int

    def __init__(self, data: str):
        self.str_to_data(data)
        if self.is_data_valid(self.day, self.month, self.year):
            print("Data is valid")
        else:
            print("Data invalid")

    @classmethod
    def str_to_data(cls, data: str):
        cls.day = int(data.split("-")[0])
        cls.month = int(data.split("-")[1])
        cls.year = int(data.split("-")[2])

    @staticmethod
    def is_data_valid(day: int, month: int, year: int):
        if (1 <= month <= 12) and (1 <= day <= monthrange(year, month)[1]):
            return True
        else:
            return False


d1 = Data("05-08-2020")
d1 = Data("31-08-2020")
d1 = Data("150-08-2020")
