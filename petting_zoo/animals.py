# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

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

Bartholomew = Llama("Bartholomew", "3 legged Peruvian Llama", "midday", "small children")
print(Bartholomew)
Bartholomew.feed()
print(f'{Bartholomew.name} the {Bartholomew.species} is available to pet during the {Bartholomew.shift} shift.')
        
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

Lassie = Pig("Lassie", "Tibetian Straight Tailed Pig", "morning", "the in-laws")
print(Lassie)
Lassie.feed()
print(f'{Lassie.name} the {Lassie.species} is available to pet during the {Lassie.shift} shift.')

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

Fluffy = Porcupine("Fluffy", "Curmudgeonly Porcupine", "afternoon", "prozac")
print(Fluffy)
Fluffy.feed()
print(f'{Fluffy.name} the {Fluffy.species} is available to pet during the {Fluffy.shift} shift.')

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

Tank = Armadillo("Tank", "Southern Yard Destroyer Armadillo", "morning", "a local golf course")
print(Tank)
Tank.feed()
print(f'{Tank.name} the {Tank.species} is available to pet during the {Tank.shift} shift.')

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

Beaudreaux = Groundhog("Beaudreaux", "Louisiana Drunken Groundhog", "afternoon", "a hobo")
print(Beaudreaux)
Beaudreaux.feed()
print(f'{Beaudreaux.name} the {Beaudreaux.species} is available to pet during the {Beaudreaux.shift} shift.')

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

Toby = Lawyers("Toby", "The Worst", "HR reports")
print(Toby)
Toby.feed()

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

Bitey = Viper("Bitey", "Pit Viper", "Roxanne's cats")
print(Bitey)
Bitey.feed()


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

Karen = Lobbyist("Karen", "Antivaxxer Lobbyist", "bubonic plague")
print(Karen)
Karen.feed()

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

Kaa = Python("Kaa", "Grey Cartoon Python", "Mowgli")
print(Kaa)
Kaa.feed()

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

Dipper = Cobra("Dipper", "Spitting Cobra", "Skoal")
print(Dipper)
Dipper.feed()

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

Wally = Gator("Wally", "Hanna Barbera Gator", "large children")
print(Wally)
Wally.feed()

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

Cuddles = Gar("Cuddles", "Eastern Brim Killer Gar", "Nemo")
print(Cuddles)
Cuddles.feed()

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

Pickles = Beaver("Pickles", "Angry Beaver", "steroids")
print(Pickles)
Pickles.feed()

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

JabberJaws = Shark("Jabber Jaws", "Great White Shark", "bachelorettes")
print(JabberJaws)
JabberJaws.feed()

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

Mechazilla = Godzilla("Mechazilla", "Robot", "a cold fusion reactor")
print(Mechazilla)
Mechazilla.feed()




