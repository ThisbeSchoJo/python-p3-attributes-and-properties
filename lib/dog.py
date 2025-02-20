#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    # define a name property
    # __init__ should recieve default argument for name
    def __init__(self, name="Thisbe", breed="Corgi"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        # name must be str
        # name must be between 1 and 25 characters
        if (isinstance(name, str)) and (1 <= len(name) <= 25):
            self._name = name
        # if name is invalid, setter method should print "Name must be string between 1 and 25 characters."
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if (breed in APPROVED_BREEDS):
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
        
    breed = property(get_breed, set_breed)
    # define a breed property
    # __init__ method should receive a default argument for breed
        # if the breed is invalid, the setter method should print:
        # "Breed must be in list of approved breeds."