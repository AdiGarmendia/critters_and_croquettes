class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "......wait!!!! Why are you running?!?! Come back!!"
        self.animals = list()

    def addAnimals(self, animals):
        self.animals.extend(animals)

    @property #getter
    def last_critter_added(self):
        return f"{self.animals[-1].name} the {self.animals[-1].species}"

class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "There are lawyers, lobbyists and snakes in there. Yes we know they suck!"
        self.animals = list()

    def addAnimals(self, animals):
        self.animals.extend(animals)
   
    @property #getter
    def last_critter_added(self):
        return f"{self.animals[-1].name} the {self.animals[-1].species}"

class WetLands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "Jaws ain't got nothing on us!!!"
        self.animals = list()


    def addAnimals(self, animals):
        self.animals.extend(animals)

    @property #getter
    def last_critter_added(self):
        return f"{self.animals[-1].name} the {self.animals[-1].species}"