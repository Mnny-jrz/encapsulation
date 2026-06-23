class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_on(self):
        return self.__on

    def set_on(self, on):
        self.__on = on


def main():
    fan1 = Fan(Fan.FAST, 10, "yellow", True)
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    print("Fan 1 → Speed:", fan1.get_speed(), "Radius:", fan1.get_radius(),
          "Color:", fan1.get_color(), "On:", fan1.is_on())
    print("Fan 2 → Speed:", fan2.get_speed(), "Radius:", fan2.get_radius(),
          "Color:", fan2.get_color(), "On:", fan2.is_on())


if __name__ == "__main__":
    main()
