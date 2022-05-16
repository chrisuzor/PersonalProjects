class Director:
    """Director"""

    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.create_new_car()
        self.builder.add_model()
        self.builder.add_tires()
        self.builder.add_engine()

    def get_car(self):
        return self.builder.car


class Builder:
    """Abstract Builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class ToyotaBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parent class"""

    def add_model(self):
        self.car.model = "Toyota"

    def add_tires(self):
        self.car.tires = "Maxdis Tires"

    def add_engine(self):
        self.car.engine = "Turbo Engine"


class Car:
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)


builder = ToyotaBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)
