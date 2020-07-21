from .animal import Animal
from movements import Walking

class Llama(Animal, Walking):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        self.shift = shift # stays on Llama because not all animals have shifts
        Walking.__init__(self)