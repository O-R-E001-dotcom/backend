class Pet:
    def __init__(self, name, species, age):
        self.name = name 
        self.species = species
        self.age = age

    def display(self):
        print(f"The pet {self.name} from the {self.species} species is {self.age} years old!")

pet1 = Pet("Rabbit", "WAD", 1)
pet1.display()