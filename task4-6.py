class TypeError(Exception):
    pass


class OfficeEquipmentWarehouse:
    office_equipment_list = {}

    def add_item(self, new_item: 'OfficeEquipment'):
        try:
            self.office_equipment_list[new_item.name] = self.office_equipment_list[new_item.name] + 1
        except KeyError:
            self.office_equipment_list[new_item.name] = 1

    def send_item_to_department(self, item: 'OfficeEquipment', d: 'OfficeEquipmentWarehouse'):
        if item.name in self.office_equipment_list:
            if self.office_equipment_list[item.name] < 1:
                print("not enough equipment")
            else:
                self.office_equipment_list[item.name] = self.office_equipment_list[item.name] - 1
                d.add_item(item)
        else:
            print("not enough equipment")

    def __str__(self):
        out_str = ""
        for key in self.office_equipment_list:
            out_str = out_str + f"{key}: {self.office_equipment_list[key]}\n"
        return out_str

    def get_info(self):
        out_str = ""
        for key in self.office_equipment_list:
            out_str = out_str + f"{key}: {self.office_equipment_list[key]}\n"

        return out_str


def Department(OfficeEquipmentWarehouse):
    name: str

    def __init__(self, name: str):
        self.name = name


class OfficeEquipment:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    pages_per_min: int
    type: str
    is_colour: bool

    def __init__(self, pages_per_min: int, eq_type: str, is_colour: bool, price: int):
        if type(pages_per_min) is not int:
            print("pages per min must be int")
            raise TypeError
        if type(eq_type) is not str:
            print("eq_type must be str")
            raise TypeError
        if type(is_colour) is not bool:
            print("is_colour must be bool")
            raise TypeError
        if type(price) is not int:
            print("price must be int")
            raise TypeError
        super().__init__("Printer", price)
        self.pages_per_min = pages_per_min
        self.type = eq_type
        self.is_colour = is_colour


class Laptop(OfficeEquipment):
    CPU: str
    GPU: str
    HDD: str

    def __init__(self, CPU: str, GPU: str, HDD: str, price: int):
        if type(CPU) is not str:
            print("CPU must be str")
            raise TypeError
        if type(GPU) is not str:
            print("GPU must be str")
            raise TypeError
        if type(HDD) is not str:
            print("HDD must be str")
            raise TypeError
        if type(price) is not int:
            print("price must be int")
            raise TypeError
        super().__init__("Laptop", price)
        self.CPU = CPU
        self.GPU = GPU
        self.HDD = HDD


wh = OfficeEquipmentWarehouse()
for i in range(0, 12):
    wh.add_item(Printer(i, "Laser", False, i ** i))
for i in range(0, 10):
    wh.add_item(Laptop("Intel", "nvidia", "WD", i ** 2))

print(wh)
