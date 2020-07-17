from animals import Llama, Pig, Porcupine, Armadillo, Groundhog, Lawyers, Viper, Lobbyist, Python, Cobra, Gator, Gar, Beaver, Shark, Godzilla
from attractions import PettingZoo, WetLands, SnakePit

Bartholomew = Llama("Bartholomew", "3 legged Peruvian Llama", "midday", "small children")
print(Bartholomew)
Bartholomew.feed()
print(f'{Bartholomew.name} the {Bartholomew.species} is available to pet during the {Bartholomew.shift} shift.')

Lassie = Pig("Lassie", "Tibetian Straight Tailed Pig", "morning", "the in-laws")
print(Lassie)
Lassie.feed()
print(f'{Lassie.name} the {Lassie.species} is available to pet during the {Lassie.shift} shift.')

Fluffy = Porcupine("Fluffy", "Curmudgeonly Porcupine", "afternoon", "prozac")
print(Fluffy)
Fluffy.feed()
print(f'{Fluffy.name} the {Fluffy.species} is available to pet during the {Fluffy.shift} shift.')

Tank = Armadillo("Tank", "Southern Yard Destroyer Armadillo", "morning", "a local golf course")
print(Tank)
Tank.feed()
print(f'{Tank.name} the {Tank.species} is available to pet during the {Tank.shift} shift.')

Beaudreaux = Groundhog("Beaudreaux", "Louisiana Drunken Groundhog", "afternoon", "a hobo")
print(Beaudreaux)
Beaudreaux.feed()
print(f'{Beaudreaux.name} the {Beaudreaux.species} is available to pet during the {Beaudreaux.shift} shift.')

Toby = Lawyers("Toby", "The Worst", "HR reports")
print(Toby)
Toby.feed()

Bitey = Viper("Bitey", "Pit Viper", "Roxanne's cats")
print(Bitey)
Bitey.feed()

Karen = Lobbyist("Karen", "Antivaxxer Lobbyist", "bubonic plague")
print(Karen)
Karen.feed()

Kaa = Python("Kaa", "Grey Cartoon Python", "Mowgli")
print(Kaa)
Kaa.feed()

Dipper = Cobra("Dipper", "Spitting Cobra", "Skoal")
print(Dipper)
Dipper.feed()

Wally = Gator("Wally", "Hanna Barbera Gator", "large children")
print(Wally)
Wally.feed()

Cuddles = Gar("Cuddles", "Eastern Brim Killer Gar", "Nemo")
print(Cuddles)
Cuddles.feed()

Pickles = Beaver("Pickles", "Angry Beaver", "steroids")
print(Pickles)
Pickles.feed()

JabberJaws = Shark("Jabber Jaws", "Great White Shark", "bachelorettes")
print(JabberJaws)
JabberJaws.feed()

Mechazilla = Godzilla("Mechazilla", "Robot", "a cold fusion reactor")
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