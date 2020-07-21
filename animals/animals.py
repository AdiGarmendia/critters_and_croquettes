# import the python datetime module to help us create a timestamp
# from datetime import date

# class Animal:
#     def __init__(self, name, species, food, chip_num):
#         self.name = name
#         self.species = species
#         self.food = food
#         self.__chip_number = chip_num
#         self.date_added = date.today()

#     def feed(self):
#         print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

#     def __str__(self):
#         return f"{self.name} is a {self.species}."

    
#     @property #getter
#     def chip_number(self):
#         try:
#             return self.__chip_number
#         except AttributeError:
#             return 0
    
#     @chip_number.setter #setter
#     def chip_number(self, new_chip_number):
#         if type(new_chip_number) is int:
#             self.__chip_number = new_chip_number
#         else:
#             raise TypeError("Just do it right.")


    # Designate Llama as a child class by adding (Animal) after the class name
# class Llama(Animal):

#     # Remove redundant properties from Llama's initialization, and set their values via Animal
#     def __init__(self, name, species, shift, food, chip_num):
#         super().__init__(name, species, food, chip_num)
#         self.shift = shift # stays on Llama because not all animals have shifts
#         self.walking = True

            
# class Pig(Animal):

#     def __init__(self, name, species, shift, food, chip_num):
#         super().__init__(name, species, food, chip_num)
#         self.shift = shift 
#         self.walking = True

# class Porcupine(Animal):

#     def __init__(self, name, species, shift, food, chip_num):
#         super().__init__(name, species, food, chip_num)
#         self.shift = shift
#         self.walking = True

# class Armadillo(Animal):

#     def __init__(self, name, species, shift, food, chip_num):
#         super().__init__(name, species, food, chip_num)
#         self.shift = shift
#         self.walking = True

#     def feed(self):
#         print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}. {self.food} is some expensive stuff!')

# class Groundhog(Animal):

#     def __init__(self, name, species, shift, food, chip_num):
#         super().__init__(name, species, food, chip_num)
#         self.shift = shift
#         self.walking = True

# class Lawyers(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.slithering = True

#     def feed(self):
#         print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} but he didnt deserve it because he is the WORST!')


# class Viper(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.slithering = True

# class Lobbyist(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.slithering = True

# class Python(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.slithering = True

# class Cobra(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.slithering = True

# class Gator(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.swimming = True

# class Gar(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.swimming = True

# class Beaver(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.swimming = True

# class Shark(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.swimming = True

# class Godzilla(Animal):

#     def __init__(self, name, species, food, chip_num ):
#         super().__init__(name, species, food, chip_num)
#         self.swimming = True

#     def feed(self):
#         print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}. {self.name} is going to bankrupt us')




