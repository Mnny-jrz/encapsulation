class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
    def get_speed(self): return self.__speed
    def set_speed(self, speed): self.__speed = speed
    # same for radius, color, on
def main():
    fan1 = Fan(Fan.FAST, 10, "yellow", True)
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)
    print("Fan1 speed:", fan1.get_speed())
    print("Fan2 speed:", fan2.get_speed())
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
