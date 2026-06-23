class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    def set_name(self, name): self.__name = name
    def get_name(self): return self.__name
    # same for type and age
