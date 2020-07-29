class Car():
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, new_speed):
        self.speed = new_speed

    def stop(self):
        self.speed = 0

    def turn(self, direction: str):
        print(f"turning {direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    _speed_limit = 60

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        return "Normal" if self.speed <= self._speed_limit else "Too high"


class WorkCar(Car):
    _speed_limit = 40

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        return "Normal" if self.speed <= self._speed_limit else "Too high"


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, True)

