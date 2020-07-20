# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

    def __init__(self, name, species, shift, food, chip_num ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.__chip_number = chip_num

    @property #getter
    def chip_number(self):
        try:
            return self.__chip_number
        except AttributeError:
            return 0
    
    @chip_number.setter #setter
    def chip_number(self, new_chip_number):
        if type(new_chip_number) is int:
            self.__chip_number = new_chip_number
        else:
            raise TypeError("Just do it right.")


    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."
        
class Pig:

    def __init__(self, name, species, shift, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.shift = shift
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Porcupine:

    def __init__(self, name, species, shift, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.shift = shift
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Armadillo:

    def __init__(self, name, species, shift, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.shift = shift
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Groundhog:

    def __init__(self, name, species, shift, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.shift = shift
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Lawyers:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is {self.species}."

class Viper:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Lobbyist:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Python:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Cobra:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Gator:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Gar:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Beaver:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Shark:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Godzilla:

    def __init__(self, name, species, food ):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."




