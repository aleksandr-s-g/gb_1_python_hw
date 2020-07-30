class OrganicCell:
    size: int

    def __init__(self, size):
        self.size = size

    def __add__(self, other: 'OrganicCell'):
        return OrganicCell(self.size + other.size)

    def __sub__(self, other: 'OrganicCell'):
        if self.size < other.size:
            print("The result is less than zero. Operation aborted.")
            return None
        return OrganicCell(self.size - other.size)

    def __mul__(self, other: 'OrganicCell'):
        return OrganicCell(self.size * other.size)

    def __truediv__(self, other: 'OrganicCell'):
        return OrganicCell(self.size // other.size)

    def make_order(self, line_len):
        out_str = ''
        for i in range(0, self.size):
            out_str = out_str + '*'
            if (i + 1) % line_len == 0:
                out_str = out_str + '\n'
        return out_str


c_arr = []
c_arr.append(OrganicCell(3))
c_arr.append(OrganicCell(7))

c_arr.append(c_arr[0] + c_arr[1])
c_arr.append(c_arr[0] - c_arr[1])
c_arr.append(c_arr[1] - c_arr[0])
c_arr.append(c_arr[0] * c_arr[1])
c_arr.append(c_arr[0] / c_arr[1])
c_arr.append(c_arr[1] / c_arr[0])

for i in range(0, len(c_arr)):
    if not c_arr[i] is None:
        print(f"{i}:{c_arr[i].size}\n{c_arr[i].make_order(5)}\n")
    else:
        print(f"{i}:None\n")
