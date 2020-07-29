import time


class TrafficLight():
    __color = "red"

    def running(self):
        print(f"now TL is {self.__color}")
        time.sleep(7)
        self.__color = "yellow"
        print(f"now TL is {self.__color}")
        time.sleep(2)
        self.__color = "green"
        print(f"now TL is {self.__color}")
        time.sleep(10)
        self.__color = "red"


tl = TrafficLight()
while True:
    tl.running()
