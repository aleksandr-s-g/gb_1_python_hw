from task4 import *

cars = [
    TownCar(10, "red", "honda fit"),
    SportCar(250, "black", "lamborgini"),
    WorkCar(50, "white", "logan"),
    PoliceCar(150, "blue", "priora")]

for car in cars:
    print(car.color, car.name, "No police" if not car.is_police else "Police", "speed is ", car.show_speed())
