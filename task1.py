import random


def create_random_matrix(size_x: int, size_y: int):
    list_arr = []
    for i in range(0, size_x):
        list = [random.randrange(0, 100) for j in range(0, size_y)]
        list_arr.append(list)
    return list_arr


class Matrix():
    data = []

    def __init__(self, list_arr: list):
        self.data = list_arr

    def __str__(self):
        out_str = ""
        for list in self.data:
            for el in list:
                out_str = out_str + str(el) + "\t"
            out_str = out_str + "\n"
        return out_str

    def __add__(self, other):
        new_list = []
        if not len(self.data) == len(other.data):
            raise KeyError
        for i in range(0, len(self.data)):
            if not len(self.data[i]) == len(other.data[i]):
                raise KeyError
            new_list.append([])
            for j in range(0, len(self.data[i])):
                new_list[i].append(self.data[i][j] + other.data[i][j])
        return Matrix(new_list)


m1 = Matrix(create_random_matrix(2, 4))
m2 = Matrix(create_random_matrix(2, 4))
m3 = m1 + m2
print(m1)
print(m2)
print(m3)
