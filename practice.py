class Pet: 
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display(self):
        print(f"Hello, the pet name is {self.name} from the {self.species} species. She is {self.age + 1} ")


pet1 = Pet("Goat", "WAD", 2)
pet1.display()