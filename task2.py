class Road():
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, mass_per_m2, thickness):
        return self._length * self._width * mass_per_m2 * thickness


r = Road(20, 5000)
print(f"{int(r.calculate_mass(25, 5) / 1000)} т.")
