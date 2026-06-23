class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # Setters
    def set_name(self, name): self.__name = name
    def set_animal_type(self, animal_type): self.__animal_type = animal_type
    def set_age(self, age): self.__age = age

    # Getters
    def get_name(self): return self.__name
    def get_animal_type(self): return self.__animal_type
    def get_age(self): return self.__age


def main():
    pet = Pet()
    pet.set_name("Buddy")
    pet.set_animal_type("Dog")
    pet.set_age(3)
    print(pet.get_name(), pet.get_animal_type(), pet.get_age())


if __name__ == "__main__":
    main()

