from animals import Llama, Pig, Porcupine, Armadillo, Groundhog, Lawyers, Viper, Lobbyist, Python, Cobra, Gator, Gar, Beaver, Shark, Godzilla
from attractions import PettingZoo, WetLands, SnakePit

Bartholomew = Llama("Bartholomew", "3 legged Peruvian Llama", "midday", "small children", 1)
print(Bartholomew)
Bartholomew.feed()
print(f'{Bartholomew.name} the {Bartholomew.species} is available to pet during the {Bartholomew.shift} shift.')

Lassie = Pig("Lassie", "Tibetian Straight Tailed Pig", "morning", "the in-laws", 2)
print(Lassie)
Lassie.feed()
print(f'{Lassie.name} the {Lassie.species} is available to pet during the {Lassie.shift} shift.')

Fluffy = Porcupine("Fluffy", "Curmudgeonly Porcupine", "afternoon", "prozac", 3)
print(Fluffy)
Fluffy.feed()
print(f'{Fluffy.name} the {Fluffy.species} is available to pet during the {Fluffy.shift} shift.')

Tank = Armadillo("Tank", "Southern Yard Destroyer Armadillo", "morning", "a local golf course", 4)
print(Tank)
Tank.feed()
print(f'{Tank.name} the {Tank.species} is available to pet during the {Tank.shift} shift.')

Beaudreaux = Groundhog("Beaudreaux", "Louisiana Drunken Groundhog", "afternoon", "a hobo", 5)
print(Beaudreaux)
Beaudreaux.feed()
print(f'{Beaudreaux.name} the {Beaudreaux.species} is available to pet during the {Beaudreaux.shift} shift.')

Toby = Lawyers("Toby", "The Worst", "HR reports", 6)
print(Toby)
Toby.feed()

Bitey = Viper("Bitey", "Pit Viper", "Roxanne's cats", 7)
print(Bitey)
Bitey.feed()

Karen = Lobbyist("Karen", "Antivaxxer Lobbyist", "bubonic plague", 8)
print(Karen)
Karen.feed()

Kaa = Python("Kaa", "Grey Cartoon Python", "Mowgli", 9)
print(Kaa)
Kaa.feed()

Dipper = Cobra("Dipper", "Spitting Cobra", "Skoal", 10)
print(Dipper)
Dipper.feed()

Wally = Gator("Wally", "Hanna Barbera Gator", "large children", 11)
print(Wally)
Wally.feed()

Cuddles = Gar("Cuddles", "Eastern Brim Killer Gar", "Nemo", 12)
print(Cuddles)
Cuddles.feed()

Pickles = Beaver("Pickles", "Angry Beaver", "steroids", 13)
print(Pickles)
Pickles.feed()

JabberJaws = Shark("Jabber Jaws", "Great White Shark", "bachelorettes", 14)
print(JabberJaws)
JabberJaws.feed()

Mechazilla = Godzilla("Mechazilla", "Robot", "a cold fusion reactor", 15)
print(Mechazilla)
Mechazilla.feed()

def report_animals_by_attractions(*attractions):

    for attraction in attractions:
        print(f'{attraction.attraction_name} is where you can find {attraction.description} ')
        for animal in attraction.animals:
            print(f'* {animal.name} the {animal.species}.')
       

varmint_village = PettingZoo("Varmint Village")
varmint_village.animals.extend([Bartholomew, Lassie, Fluffy, Beaudreaux, Tank])
for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}.')


slither_inn = SnakePit("Slither Inn")
slither_inn.animals.extend([Toby, Bitey, Karen, Kaa, Dipper])
for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}.')


danger_bay = WetLands("Danger Bay")
danger_bay.animals.extend([Wally, Cuddles, JabberJaws, Pickles, Mechazilla])
for animal in danger_bay.animals:
    print(f'You can find {animal.name} the {animal.species} in {danger_bay.attraction_name}.')

report_animals_by_attractions(danger_bay, slither_inn, varmint_village)

print(Bartholomew.chip_number)
print(danger_bay.last_critter_added)
