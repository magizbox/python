class Dog:
    """one ò the objects to be returned"""
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food"

class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects return by the DogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))

# Create a Concrete Factory
factory = DogFactory()

# Create a pet store housing our Abstract factory
shop = PetStore(factory)

# Invode the utility  