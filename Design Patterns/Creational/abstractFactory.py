class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"


class PetStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        """pet factory is our Abstract Factory"""
        self.pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned"""
        pet = self.pet_factory.get_pet()
        pet_food = self.pet_factory.get_food()
        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))


# Create a concrete Factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
shop = PetStore(factory)

# Invoke the utility method to show the details of our pet
shop.show_pet()
