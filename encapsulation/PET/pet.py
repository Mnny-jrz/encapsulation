class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    def set_name(self, name): self.__name = name
    def get_name(self): return self.__name
    # same for type and age
def main():
    pet = Pet()
    pet.set_name("Buddy")
    pet.set_animal_type("Dog")
    pet.set_age(3)
    print(pet.get_name(), pet.get_animal_type(), pet.get_age())
